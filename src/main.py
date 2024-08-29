import requests
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Obter a chave da API do Fortnite
api_key = os.getenv("FORTNITE_API_KEY")

def get_fortnite_shop():
    api_url = "https://fortniteapi.io/v1/shop?lang=en"
    headers = {"Authorization": api_key}
    response = requests.get(api_url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Erro na requisição: {response.status_code}")

def recommend_skins(shop_data):
    print("Dados da loja:", shop_data)  # Verifica o conteúdo completo
    items = shop_data.get('data', [])  # Acessa a lista de itens
    print("Itens disponíveis:", items)  # Verifica os itens disponíveis
    skins = [item for item in items if item.get('type') == 'outfit']  # Filtra por tipo 'outfit'
    print("Skins filtradas:", skins)  # Verifica as skins filtradas
    if not skins:
        print("Nenhuma skin recomendada encontrada.")
    else:
        print("Skins recomendadas:")
        for skin in skins:
            print(f"Nome: {skin['name']}, Raridade: {skin['rarity']}")

if __name__ == '__main__':
    try:
        shop_data = get_fortnite_shop()
        recommend_skins(shop_data)
    except Exception as e:
        print(f"Erro: {e}")