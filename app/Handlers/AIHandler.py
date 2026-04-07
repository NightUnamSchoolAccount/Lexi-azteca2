from dotenv import load_dotenv
import os
import requests

class AIHandler:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv('DEEPSEEK_API_KEY')
        self.api_url = "https://api.deepseek.com/chat/completions"
        self.model = "deepseek-chat"  # o "deepseek-reasoner" para el modelo R1

    def generate_response(self, prompt):
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        data = {
            "model": self.model,
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "max_tokens": 150
        }
        response = requests.post(self.api_url, headers=headers, json=data)

        if response.status_code == 200:
            return response.json()['choices'][0]['message']['content']
        else:
            raise Exception(f"Error en la API: {response.status_code} - {response.text}")