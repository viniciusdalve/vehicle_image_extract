#!/usr/bin/env python3

import os
import base64
from pydantic import BaseModel, Field
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.runnables import chain
from dotenv import load_dotenv

load_dotenv()  # Carrega as variáveis do .env

import os
openai_api_key = os.getenv("OPENAI_API_KEY")

# ==========================================
# 1) Modelo Pydantic para validação
# ==========================================

class Vehicle(BaseModel):
    Type: str = Field(..., examples=["Car", "Truck", "Motorcycle", "Bus", "Van"])
    License: str = Field(..., description="License plate number.")
    Make: str = Field(..., examples=["Toyota", "Honda", "Ford", "Suzuki"])
    Model: str = Field(..., examples=["Corolla", "Civic", "F-150"])
    Color: str = Field(..., example=["Red", "Blue", "Black", "White"])

# Parser JSON baseado no modelo Pydantic
parser = JsonOutputParser(pydantic_object=Vehicle)
instructions = parser.get_format_instructions()

# ==========================================
# 2) Função para processar a imagem enviada
# ==========================================

def image_encoding(inputs):
    """Carrega e converte imagem para base64"""
    image_path = inputs["image_path"]  # Acessa o caminho da imagem corretamente

    with open(image_path, "rb") as image_file:
        image_base64 = base64.b64encode(image_file.read()).decode("utf-8")
    
    return {"image": image_base64}

@chain
def prompt(inputs):
    """Cria o prompt para o modelo GPT analisar a imagem"""
    return [
        SystemMessage(content=
            "You are an AI assistant whose job is to inspect an image and provide "
            "the desired information from the image. If the desired field is not "
            "clear or not well detected, return None for this field. Do not try to guess."
        ),
        HumanMessage(
            content=[
                {"type": "text", "text": "Examine the main vehicle type, license plate number, make, model and color."},
                {"type": "text", "text": instructions},
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{inputs['image']}", "detail": "low"}}
            ]
        )
    ]

@chain
def MLLM_response(inputs):
    """Invoca o modelo GPT para extrair informações da imagem"""
    model = ChatOpenAI(model="gpt-4o-2024-08-06", temperature=0.0, max_tokens=1024)
    output = model.invoke(inputs)
    return output.content



# Monta o pipeline
pipeline = image_encoding | prompt | MLLM_response | parser
