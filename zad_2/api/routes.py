from flask import Blueprint, request, jsonify
from models import db, Person

api_bp = Blueprint('jobs', __name__)


@api_bp.route('/<int:job_id>', methods=['GET'])
def get_job(job_id):
    job = Person.query.get(job_id)
    if not job:
        return jsonify({'error': 'Not found'}), 404

    answer = {
        'id': job.id,
        'name': job.name,
        'work': job.work
    }
    return jsonify(answer)