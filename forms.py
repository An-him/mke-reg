from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, RadioField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class RegistrationForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    gender = SelectField('Gender', choices=[('male', 'Male'), ('female', 'Female')], validators=[DataRequired()])
    phone_number = StringField('Phone Number', validators=[DataRequired(), Length(min=10, max=10)])
    residence = StringField('Residence', validators=[DataRequired()])
    serving = RadioField('Are you serving with us?', choices=[('yes', 'Yes'), ('no', 'No')], default='no', validators=[DataRequired()])
    team = RadioField('Team', choices=[('team1', 'Team 1'), ('team2', 'Team 2'), ('team3', 'Team 3'), ('team4', 'Team 4'), ('team5', 'Team 5'), ('team6', 'Team 6')], validators=[DataRequired()])
    student = RadioField('Are you a student?', choices=[('yes', 'Yes'), ('no', 'No')], default='no', validators=[DataRequired()])
    first_time = RadioField('Is this your first time?', choices=[('yes', 'Yes'), ('no', 'No')], default='no', validators=[DataRequired()])
    consent = BooleanField('I consent to the terms and conditions', validators=[DataRequired()])
    submit = SubmitField('Register')