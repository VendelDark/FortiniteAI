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

def get_all_items(shop_data):
    items = shop_data.get('featured', []) + shop_data.get('daily', []) + shop_data.get('special', [])
    return items

def item_matches_preferences(item, preferences):
    # Verifica o tipo do item
    if item.get('type') not in preferences['preferred_types']:
        return False

    # Verifica a raridade do item
    if item.get('rarity') not in preferences['preferred_rarities']:
        return False

    # Verifica o preço do item
    if item.get('price', 0) > preferences['max_price']:
        return False

    return True

def recommend_items(shop_data, user_preferences):
    items = get_all_items(shop_data)
    recommended_items = []

    for item in items:
        if item_matches_preferences(item, user_preferences):
            recommended_items.append(item)

    return recommended_items

if __name__ == '__main__':
    try:
        shop_data = get_fortnite_shop()
        print(recommend_items(shop_data, {
            'preferred_types': ['outfit', 'weapon', 'backpack'],
            'preferred_rarities': ['legendary', 'epic'],
            'max_price': 2000
        }))
    except Exception as e:
        print(f"Erro: {e}")