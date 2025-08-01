# CAMBIO-PY! Currency converter with Flask

Este projeto é um conversor de moedas simples que usa Flask para o backend e uma API externa para obter taxas de câmbio atualizadas.

## Funcionalidades

- Exibe taxas de câmbio baseadas no dólar americano (USD).
- Permite o usuário converter um valor entre duas moedas diferentes.
- Também mostra ao usuário uma lista de todas as moedas em relação a 1 dólar americano(USD).

## Tecnologias usadas

- Python 3.x  
- Flask  
- requests  
- python-dotenv  
- API ExchangeRate-API (https://www.exchangerate-api.com/)

## Como usar

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

