from flask import Blueprint, request, jsonify
from models import db, Person

api_bp = Blueprint('api', __name__)

from flask import jsonify

@api_bp.route('/add_user', methods=['POST', 'GET'])
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


@api_bp.route('/job/<job_id>', methods=['GET'])
def get_job(job_id):
    # Проверяем, что job_id состоит только из цифр
    if not job_id.isdigit():
        return jsonify({
            'error': 'Неверный формат ID',
            'message': 'ID должен быть целым числом'
        }), 400  # HTTP 400 - Bad Request

    # Преобразуем в число
    job_id_int = int(job_id)

    # Ищем запись в базе
    job = Person.query.get(job_id_int)

    if not job:
        return jsonify({
            'error': 'Запись не найдена',
            'message': f'Нет записи с ID {job_id_int}'
        }), 404  # HTTP 404 - Not Found

    # Если всё ок - возвращаем данные
    return jsonify({
        'id': job.id,
        'name': job.name,
        'work': job.work
    })


@api_bp.route('/jobs', methods=['GET'])
def get_jobs():
    jobs = Person.query.all()
    answ_list = []
    for job in jobs:
        answer = {
            'id': job.id,
            'name': job.name,
            'work': job.work
        }
        answ_list.append(answer)
    return jsonify(answ_list)