import requests
from dotenv import load_dotenv
import os
from googletrans import Translator

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Obter a chave da API do Fortnite
api_key = os.getenv("FORTNITE_API_KEY")

# Função para obter dados da loja Fortnite
def get_fortnite_shop():
    api_url = "https://fortniteapi.io/v1/shop?lang=en"
    headers = {"Authorization": api_key}
    response = requests.get(api_url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Erro na requisição: {response.status_code}")

# Função para obter todos os itens da loja
def get_all_items(shop_data):
    items = shop_data.get('featured', []) + shop_data.get('daily', []) + shop_data.get('special', [])
    return items

# Função para verificar se o item corresponde às preferências
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

# Função para traduzir a descrição dos itens
def translate_description(description, target_lang='pt'):
    translator = Translator()
    try:
        translated = translator.translate(description, dest=target_lang)
        return translated.text
    except Exception as e:
        print(f"Erro na tradução: {e}")
        return description  # Retorna a descrição original em caso de erro

# Função para recomendar itens com base nas preferências do usuário
def recommend_items(shop_data, user_preferences):
    items = get_all_items(shop_data)
    recommended_items = []

    for item in items:
        if item_matches_preferences(item, user_preferences):
            # Traduz a descrição dos itens
            item['description'] = translate_description(item.get('description', ''), target_lang='pt')
            recommended_items.append(item)

    return recommended_items

if __name__ == '__main__':
    try:
        shop_data = get_fortnite_shop()
        recommended_items = recommend_items(shop_data, {
            'preferred_types': ['outfit', 'weapon', 'backpack'],
            'preferred_rarities': ['legendary', 'epic'],
            'max_price': 2000
        })
        for item in recommended_items:
            print(item)
    except Exception as e:
        print(f"Erro: {e}")