import requests

API_URL = 'https://v6.exchangerate-api.com/v6/YOUR-API-KEY/latest/USD'
#a chave fica em um arquivo .env! coloquei esse exemplo simples pq vou construir o arquivo ainda

response = requests.get(API_URL)
data = response.json()

print(data)