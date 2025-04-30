import flask
from flask import jsonify
from flask_login import login_required
from models import Work, User

blueprint = flask.Blueprint(
    'works_api',
    __name__,
    template_folder='templates'
)

@blueprint.route('/works')
@login_required
def get_works():
    works = Work.query.all()
    result = []
    for work in works:
        user = User.query.get(work.user_id)
        result.append({
            'id': work.id,
            'description': work.description,
            'user_id': work.user_id,
            'user_name': user.name if user else None
        })
    return jsonify({'works': result})