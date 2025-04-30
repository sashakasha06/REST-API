from flask import Flask, render_template
from models import db, Person
from api.routes import api_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Инициализация БД
db.init_app(app)

# Создаём таблицы вручную
with app.app_context():
    db.create_all()

# Регистрация Blueprint
app.register_blueprint(api_bp, url_prefix='/api')

@app.route('/')
def home():
    people = Person.query.all()  # Теперь таблица точно существует
    return render_template('home.html', people=people)

if __name__ == '__main__':
    app.run(debug=True)