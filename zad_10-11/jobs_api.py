from flask import Blueprint, jsonify
from models import db, Work, User
from flask_login import login_required

works_api = Blueprint('works_api', __name__)


@works_api.route('/api/jobs')
@login_required
def get_jobs():
    works = Work.query.all()

    result = []
    for work in works:
        user = User.query.get(work.user_id)
        result.append({
            'id': work.id,
            'description': work.description,
            'user_id': work.user_id,
            'user_name': user.name if user else None,
            'created_at': work.created_at.isoformat() if work.created_at else None
        })

    return jsonify({'jobs': result})