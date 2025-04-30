from flask import Blueprint, request, jsonify
from models import db, Person

api_bp = Blueprint('api', __name__)


@api_bp.route('/data', methods=['POST'])
def add_data():
    data = request.get_json()

    if not data or 'name' not in data or 'age' not in data:
        return jsonify({"error": "Name and age are required!"}), 400

    new_person = Person(
        name=data['name'],
        age=data['age'],
        work=data.get('work', '')  # work не обязателен
    )

    db.session.add(new_person)
    db.session.commit()

    return jsonify({"message": "Data added successfully!"})