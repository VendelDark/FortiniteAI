from flask import Flask, render_template, jsonify
from main import get_fortnite_shop, recommend_items

app = Flask(__name__)

# Dados de preferência do usuário (podem ser ajustados dinamicamente)
user_preferences = {
    'preferred_types': ['outfit', 'weapon', 'backpack', 'glider', 'wrap', 'pickaxe', 'contrail'],
    'preferred_rarities': ['mythic', 'legendary', 'epic', 'rare', 'uncommon', 'common'],
    'max_price': 2000
}

@app.route('/')
def home():
    try:
        shop_data = get_fortnite_shop()
        items = recommend_items(shop_data, user_preferences)
        return render_template('index.html', items=items)
    except Exception as e:
        return f"Erro: {e}"

@app.route('/api/items')
def api_items():
    try:
        shop_data = get_fortnite_shop()
        items = recommend_items(shop_data, user_preferences)
        return jsonify(items)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)