from flask import Flask, url_for, render_template, redirect, request, flash, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'flash message'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/crud'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class list(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

@app.route('/', methods = ['GET', 'POST'])
def index():

    all_data = list.query.all()

    return render_template('index.html', rows = all_data)

@app.route('/insert', methods = ['GET', 'POST'])
def insert():

    if request.method == 'POST':
        name  = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        my_data = list(name, email, phone)
        db.session.add(my_data)
        db.session.commit()

        flash("Data Inserted Successfully")

        return redirect(url_for('index'))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)