from flask import Blueprint, jsonify
from main import get_fortnite_shop, recommend_skins

skins_bp = Blueprint('skins', __name__)

@skins_bp.route('/api/skins', methods=['GET'])
def get_skins():
    try:
        shop_data = get_fortnite_shop()
        skins = recommend_skins(shop_data)
        return jsonify(skins)
    except Exception as e:
        return jsonify({"error": str(e)}), 500