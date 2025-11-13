import os
import requests
from dotenv import load_dotenv

load_dotenv()

endpoint = os.getenv("AZURE_ENDPOINT")
key = os.getenv("AZURE_KEY")

headers = {
    "Ocp-Apim-Subscription-Key": key,
    "Content-Type": "application/json"
}

documents = {
    "documents": [
        {"id": "1", "language": "pt", "text": "Estou muito feliz com o serviço!"},
        {"id": "2", "language": "pt", "text": "O produto chegou quebrado, estou decepcionado."}
    ]
}

response = requests.post(
    f"{endpoint}/text/analytics/v3.1/sentiment",
    headers=headers,
    json=documents
)

print(response.json())
