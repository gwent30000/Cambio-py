# CAMBIO-PY! Currency converter with Flask

Este projeto é um conversor de moedas simples que usa Flask para o backend e uma API externa para obter taxas de câmbio atualizadas.

## Funcionalidades

- Exibe taxas de câmbio baseadas no dólar americano (USD).
- Permite o usuário converter um valor entre duas moedas diferentes.
- Também mostra ao usuário uma lista de todas as moedas em relação a 1 dólar americano(USD).

## 🛠 Tecnologias usadas

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Framework-black?logo=flask)
![Requests](https://img.shields.io/badge/Requests-HTTP%20Client-yellow)
![python-dotenv](https://img.shields.io/badge/dotenv-Environment%20Variables-green)
[![API](https://img.shields.io/badge/API-ExchangeRateAPI-orange)](https://www.exchangerate-api.com/)

## Como funciona(EXPLICAÇÃO PARA A VERSÃO COMPLETA)

Carrega a API key
O código pega a chave da API (API_KEY) que você guarda no arquivo .env, para poder consultar ela.

E na rota principal (/) - homepage
Quando alguém abre a página, o backend faz uma requisição para a API externa de câmbio que recebe as taxas de conversão atualizadas e manda esses dados para o arquivo index.html.
Esses dados vêm numa variável chamada exchange_data.

![Print da tela](https://github.com/gwent30000/Cambio-py/blob/eb86c08f07b2f1b66a0907463979bba2a0b26ba1/conversor-moedas/img/3342544.png)

![Print da tela](https://github.com/gwent30000/Cambio-py/blob/eb86c08f07b2f1b66a0907463979bba2a0b26ba1/conversor-moedas/img/Captura%20de%20tela%202025-08-01%20225615.png)

Rota de conversão (/converter) - converter
Quando o usuário enviar o formulário no site com:

    moeda_origem (ex: "USD")

    moeda_destino (ex: "BRL")

    valor (ex: 100)

O backend faz outra requisição para a API para garantir que as taxas estão atualizadas. Depois ele pega as taxas para as duas moedas escolhidas.

- Cálculo da conversão
Como a API sempre tem as taxas baseadas no USD, o código:

    converte o valor enviado para USD (dividindo pelo valor da taxa da moeda de origem)

    converte o valor em USD para a moeda destino (multiplicando pela taxa da moeda destino)

- Resultado enviado para o frontend
O valor convertido (arredondado com 2 casas decimais) é enviado para o index.html junto com as taxas atualizadas para mostrar pro usuário.

![Print da tela](https://github.com/gwent30000/Cambio-py/blob/main/conversor-moedas/img/PRINT02.png)

### Pré-requisitos

- Ter Python instalado.  
- Obter uma chave de API gratuita em https://www.exchangerate-api.com/  
- Criar um arquivo `.env` na raiz do projeto com a chave assim:

API_KEY=SUA_CHAVE_AQUI

### Rodar o projeto

1. Instale as dependências:

```bash
pip install -r requirements.txt
```

2. Execute o app:

```bash
python main.py
```

3. Abra no navegador:

```bash
http://127.0.0.1:5000/
```

### Possíveis melhorias futuras

    Validação de dados no frontend.

    Estilização CSS para melhorar o visual.

