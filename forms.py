from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, RadioField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length


class RegistrationForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    gender = RadioField('Gender', choices=[
        ('male', 'Male'), ('female', 'Female')], validators=[DataRequired()])
    phone_number = StringField('Phone Number', validators=[
                               DataRequired(), Length(min=10, max=12)])
    residence = StringField('Residence', validators=[DataRequired()])
    serving = RadioField('Are you serving with us?', choices=[
                         ('yes', 'Yes'), ('no', 'No')], default='no', validators=[DataRequired()])
    team = RadioField('Team', choices=[('administration', 'Administration'), ('welfare', 'Welfare'), ('communications', 'Communications'), (
        'missions', 'Missions and Outreach'), ('operations', 'Operations'), ('legal', 'Legal'), ('finance', 'Finance')], validators=[DataRequired()])
    student = RadioField('Are you a student?', choices=[
                         ('yes', 'Yes'), ('no', 'No')], default='no', validators=[DataRequired()])
    institution_name = StringField(
        'Name of Institution', validators=[DataRequired()])
    institution_location = StringField(
        'Location of Institution', validators=[DataRequired()])
    first_time = RadioField('Is this your first time?', choices=[(
        'yes', 'Yes'), ('no', 'No')], default='no', validators=[DataRequired()])
    consent = BooleanField(
        'I consent to the terms and conditions', validators=[DataRequired()])
    submit = SubmitField('Submit')
