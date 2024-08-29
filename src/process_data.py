import csv
import json
import os

# Caminho para o arquivo JSON
json_file_path = os.path.join(os.path.dirname(__file__), '../data/data.json')

# Caminho para o arquivo CSV
csv_file_path = os.path.join(os.path.dirname(__file__), '../data/processed_items.csv')

def process_data():
    # Verificar se o arquivo JSON existe
    if not os.path.isfile(json_file_path):
        raise FileNotFoundError(f"File not found: {json_file_path}")

    # Ler dados JSON
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    # Abrir o arquivo CSV para escrita
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Escrever o cabeçalho do CSV
        header = [
            'id', 'name', 'description', 'type', 'rarity', 'internalRarity', 'price',
            'priceNoDiscount', 'categories', 'priority', 'banner', 'offer', 'releaseDate',
            'lastAppearance', 'interest', 'giftAllowed', 'buyAllowed', 'image', 'icon',
            'full_background', 'items', 'otherItemsDetails', 'videos', 'customColors'
        ]
        writer.writerow(header)

        # Iterar sobre os itens em 'featured' e escrever no CSV
        for item in data.get('featured', []):
            writer.writerow([
                item.get('id', ''),
                item.get('name', ''),
                item.get('description', ''),
                item.get('type', ''),
                item.get('rarity', ''),
                item.get('internalRarity', ''),
                item.get('price', ''),
                item.get('priceNoDiscount', ''),
                item.get('categories', ''),
                item.get('priority', ''),
                item.get('banner', ''),
                item.get('offer', ''),
                item.get('releaseDate', ''),
                item.get('lastAppearance', ''),
                item.get('interest', ''),
                item.get('giftAllowed', ''),
                item.get('buyAllowed', ''),
                item.get('image', ''),
                item.get('icon', ''),
                item.get('full_background', ''),
                ', '.join(item.get('items', [])),
                json.dumps(item.get('otherItemsDetails', [])),
                json.dumps(item.get('videos', [])),
                json.dumps(item.get('customColors', {}))
            ])

if __name__ == '__main__':
    process_data()