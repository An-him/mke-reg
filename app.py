from flask import Flask, render_template, request, redirect, url_for
import csv
import json
from forms import RegistrationForm
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///registrations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Registration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    gender = db.Column(db.String(10))
    phone_number = db.Column(db.String(15))
    residence = db.Column(db.String(100))
    serving = db.Column(db.String(3))
    teams = db.Column(db.String(100))
    student = db.Column(db.String(3))
    first_time = db.Column(db.String(3))
    consent = db.Column(db.String(3))


with app.app_context():
    db.create_all()


app.config['SECRET_KEY'] = 'your_secret_key'


@app.route('/', methods=['GET', 'POST'])
def registration():
    # if request.method == 'POST':
    form = RegistrationForm()

    # db.session.add(form)
    # db.session.commit()

    # return redirect(url_for('thank_you'))

    return render_template('registration.html', form=form)


@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')


if __name__ == '__main__':
    app.run(debug=True)
