from flask import Blueprint, jsonify
from models import Work, User

works_blueprint = Blueprint('works_api', __name__)

@works_blueprint.route('/works')
def get_works():
    works = Work.query.all()
    result = [
        {
            'id': work.id,
            'description': work.description,
            'user_id': work.user_id,
            'user_name': User.query.get(work.user_id).name if User.query.get(work.user_id) else None
        }
        for work in works
    ]
    return jsonify({'works': result})