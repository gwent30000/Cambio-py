import requests
from flask import Flask, render_template, request
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_URL = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD'

def init_app(app):
    @app.route('/')
    def homepage():
        response = requests.get(API_URL)
        api_response = response.json()
        return render_template('index.html', exchange_data=api_response)

    @app.route('/converter', methods=['POST'])
    def converter():
        moeda_origem = request.form['moeda_origem']
        moeda_destino = request.form['moeda_destino']
        valor = float(request.form['valor'])

        response = requests.get(API_URL)
        api_response = response.json()

        rates = api_response['conversion_rates']
        source_to_usd = rates[moeda_origem]
        target_to_usd = rates[moeda_destino]

        usd_amount = valor / source_to_usd
        converted_amount = usd_amount * target_to_usd

        return render_template('index.html',exchange_data=api_response,
        result=round(converted_amount, 2)
        )
