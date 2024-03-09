from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

users = {}

user_id_counter = 1


@app.route('/', methods=['GET', 'POST'])
def registration():
    global user_id_counter
    if request.method == 'POST':
        first_name = request.form.get('first_name', '')
        last_name = request.form.get('last_name', '')
        gender = request.form.get('gender', '')
        phone_number = request.form.get('phone_number', '')
        residence = request.form.get('residence', '')
        serving = request.form.get('serving', 'no')
        teams = request.form.getlist('team')
        student = request.form.get('student', 'no')
        first_time = request.form.get('first_time', 'no')
        consent = request.form.get('consent', '')

        # Store the user's information in the database
        user_data = {
            'first_name': first_name,
            'last_name': last_name,
            'gender': gender,
            'phone_number': phone_number,
            'residence': residence,
            'serving': serving,
            'teams': teams,
            'student': student,
            'first_time': first_time,
            'consent': consent
        }

        # Append user data to the users dictionary with a unique identifier
        users[user_id_counter] = user_data

        # Increment user id counter
        user_id_counter += 1

        return redirect(url_for('thank_you'))

    return render_template('registration.html')


@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')


if __name__ == '__main__':
    app.run(debug=True)
