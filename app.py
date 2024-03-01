from flask import Flask, render_template
from flask_migrate import Migrate
from models import db
from database_operations import fetch_all_publications

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:M@1122919448@localhost:5432/PostgreSQL15"
db.init_app(app)
# migrate = Migrate(app, db)

@app.route('/')
def index():
    solution = fetch_all_publications()
    print(solution)
    return render_template('index.html', publications=solution)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
