import requests
import json
import time
from datetime import datetime

# Configuração da API da Binance
BINANCE_SYMBOL = "BTCUSDT"
RESULTS_FILE = "dados_monitoramento.txt"

# Função para salvar dados em um arquivo txt
def save_to_file(data):
    with open(RESULTS_FILE, "a", encoding="utf-8") as file:
        file.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]\n")
        file.write(data + "\n\n")

# Função para ler o arquivo txt
def read_from_file():
    try:
        with open(RESULTS_FILE, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return "Arquivo de resultados ainda não existe."

# Função para obter preço do Bitcoin na Binance
def get_crypto_price():
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={BINANCE_SYMBOL}"
    response = requests.get(url)
    data = response.json()
    
    if "price" in data:
        return float(data["price"])
    else:
        print("Erro ao obter preço da Binance")
        return None

# Loop de monitoramento
def monitor_data():
    while True:
        print("\n[INFO] Coletando dados do Bitcoin...")
        crypto_price = get_crypto_price()
        
        if crypto_price is not None:
            result = f"Preço atual do {BINANCE_SYMBOL}: {crypto_price} USDT"
            print(result)
            save_to_file(result)
        
        time.sleep(600)  # Espera 10 minutos antes da próxima coleta

# Iniciar monitoramento
if __name__ == "__main__":
    monitor_data()