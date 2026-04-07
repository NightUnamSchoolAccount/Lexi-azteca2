from dotenv import load_dotenv
import os
import requests

class AiHandler:
    def __init__(self):
        load_dotenv()  # Carga las variables de entorno desde el archivo .env
        self.api_key = os.getenv('API_KEY_IA')  # Asegúrate de que esta variable de entorno esté configurada correctamente
        self.api_url = "https://api.ejemplo.com/generate"  # Reemplaza con la URL real de tu API de IA

    def generate_response(self, prompt):
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        data = {
            'prompt': prompt,
            'max_tokens': 150
        }
        response = requests.post(self.api_url, headers=headers, json=data)
        
        if response.status_code == 200:
            return response.json().get('choices', [{}])[0].get('text', '')
        else:
            raise Exception(f"Error en la API: {response.status_code} - {response.text}")