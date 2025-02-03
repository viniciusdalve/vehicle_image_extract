
🚗 MyVehicleApp - Identificação e Registro de Veículos
📌 Sobre o Projeto
MyVehicleApp é um aplicativo móvel desenvolvido com React Native (Expo) que permite capturar e enviar imagens de veículos para um servidor backend FastAPI. O backend utiliza LangChain + OpenAI para extrair informações como placa, marca, modelo, cor e localização (estado/cidade) a partir da imagem da placa do veículo.

🔥 Principais Funcionalidades
✅ Captura de Imagem: Tire uma foto do veículo diretamente pela câmera 📷
✅ Galeria: Escolha uma imagem da galeria 🖼️
✅ Processamento via API: Envie a imagem para análise no servidor 🌍
✅ Extração de Dados:

Placa do veículo 🔢
Marca e Modelo 🚗
Cor do veículo 🎨
Hora da análise ⏰
Localização baseada na placa (Cidade/Estado) 🏙️
✅ Interface moderna e responsiva com styled-components e React Native Paper
🏗 Tecnologias Utilizadas
📱 Mobile (Frontend)
🚀 React Native com Expo
🎨 Styled-Components para estilização
📝 React Native Paper para UI
📷 Expo ImagePicker para seleção de imagens
🌐 Fetch API para comunicação com o backend
🖥 Backend (API)
⚡ FastAPI para a API REST
🧠 LangChain + OpenAI para extração de dados das imagens
🔍 Pydantic para validação de dados
🚀 Uvicorn para servir a API
🛠 Como Rodar o Projeto
📱 Executando o App Mobile
Clone o repositório:
sh
Copiar
Editar
git clone https://github.com/seu-usuario/myVehicleApp.git
cd myVehicleApp
Instale as dependências:
sh
Copiar
Editar
npm install
Inicie o Expo:
sh
Copiar
Editar
npx expo start
Escaneie o QR Code no Expo Go para rodar no celular.
🖥 Executando o Backend
Acesse a pasta do backend:
sh
Copiar
Editar
cd backend
Instale as dependências:
sh
Copiar
Editar
pip install -r requirements.txt
Rode o servidor FastAPI:
sh
Copiar
Editar
uvicorn controller:app --host 0.0.0.0 --port 8000 --reload
Acesse a API no navegador:
bash
Copiar
Editar
http://localhost:8000/docs
📌 Próximos Passos
📍 Melhorar a precisão da identificação da placa e localização
📍 Adicionar suporte para armazenar logs de veículos analisados
📍 Implementar autenticação de usuários para gerenciar registros

