from flask import Flask, render_template, request, redirect, url_for
import csv
import os
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
    if form.validate_on_submit():
        print("Form submitted successfully!")
        try:
            # Get form data
            first_name = form.first_name.data
            last_name = form.last_name.data
            gender = form.gender.data
            phone_number = form.phone_number.data
            residence = form.residence.data
            serving = form.serving.data
            team = form.team.data
            student = form.student.data
            institution_name = form.institution_name.data
            institution_location = form.institution_location.data
            first_time = form.first_time.data
            consent = form.consent.data

            # Write form data to CSV file
            filename = 'registrations.csv'
            file_exists = os.path.exists(filename)

            # Write form data to CSV file
            with open('registrations.csv', 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                if not file_exists:  # Write header if file is newly created
                    writer.writerow(['First Name', 'Last Name', 'Gender', 'Phone Number', 'Residence', 'Serving',
                                    'Team', 'Student', 'Institution Name', 'Institution Location', 'First Time', 'Consent'])
                writer.writerow([first_name, last_name, gender, phone_number, residence, serving,
                                team, student, institution_name, institution_location, first_time, consent])

            return redirect(url_for('thank_you'))
        except Exception as e:
            print(f"Error occurred while writing to CSV file: {str(e)}")

    # db.session.add(form)
    # db.session.commit()
    print(form.errors)
    return render_template('registration.html', form=form)


@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')


if __name__ == '__main__':
    app.run(debug=True)
