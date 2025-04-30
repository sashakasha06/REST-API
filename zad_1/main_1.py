from flask import Flask
from flask_login import LoginManager
from models import db, User, Work
from works_api import works_blueprint

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Важно: сначала инициализируем db с приложением
db.init_app(app)

login_manager = LoginManager(app)

def init_db():
    with app.app_context():  # Создаем контекст приложения
        db.create_all()

        if not User.query.filter_by(email='test@test.ru').first():
            test_user = User(
                email='test@test.ru',
                name='Test User'
            )
            test_user.set_password('Password12345')
            db.session.add(test_user)

            test_user2 = User(
                email='test2@test.ru',
                name='Test User2'
            )
            test_user2.set_password('Password54321')
            db.session.add(test_user2)

            test_user3 = User(
                email='test3@test.ru',
                name='Test User3'
            )
            test_user3.set_password('Password54')
            db.session.add(test_user3)
            db.session.flush()

            work1 = Work(id=1, description="Пример описания 1", user_id=test_user.id)
            work2 = Work(id=2, description="Пример описания 2", user_id=test_user2.id)
            work3 = Work(id=3, description="Пример описания 3", user_id=test_user2.id)
            work4 = Work(id=4, description="Пример описания 4", user_id=test_user2.id)
            db.session.add(work1)
            db.session.add(work2)
            db.session.add(work3)
            db.session.add(work4)
            db.session.commit()

# Регистрируем blueprint после инициализации приложения
app.register_blueprint(works_blueprint, url_prefix='/api')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

if __name__ == '__main__':
    init_db()  # Инициализируем базу данных
    app.run(debug=True)