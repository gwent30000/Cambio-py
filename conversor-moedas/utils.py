import requests
from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_URL = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD'

def init_app(app):
    @app.route('/')
    def homepage():
        response = requests.get(API_URL)
        return response.json()

