from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import os
import shutil
from main import pipeline  # Importa o pipeline do `main.py`

app = FastAPI()

# Dicionário de tradução de cores
color_translation = {
    "Red": "Vermelho",
    "Blue": "Azul",
    "Black": "Preto",
    "White": "Branco",
    "Silver": "Prata",
    "Gray": "Cinza",
    "Green": "Verde",
    "Yellow": "Amarelo",
    "Orange": "Laranja",
    "Brown": "Marrom",
    "Purple": "Roxo",
    "Pink": "Rosa"
}

# Ajustando a resposta do pipeline para traduzir a cor
def translate_vehicle_data(data):
    """ Traduz a cor do veículo para português antes de enviar a resposta """
    data["Color"] = color_translation.get(data.get("Color", ""), "Desconhecido")  # Traduzindo cor
    return data

# No controller.py (ou onde estiver chamando o pipeline)
@app.post("/analyze")
async def analyze_vehicle(file: UploadFile = File(...)):
    temp_path = f"temp_{file.filename}"
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    result = pipeline.invoke({"image_path": temp_path})  # Processa a imagem
    os.remove(temp_path)

    # Traduz a cor do veículo antes de retornar
    translated_result = translate_vehicle_data(result)

    return JSONResponse(content=translated_result)

