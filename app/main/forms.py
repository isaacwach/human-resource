from flask_wtf import FlaskForm
from wtforms import TextAreaField,SubmitField, StringField
from wtforms.validators import DataRequired,Email,EqualTo
from ..models import User


# class RegisterUser(FlaskForm):

class CreateProfile(FlaskForm):
    fullname = StringField('Enter your full name',validators = [DataRequired()])
    position = TextAreaField('Write your Blog ',validators=[DataRequired()])
    job_id = StringField('Enter your full name',validators = [DataRequired()])
    department = StringField('Enter your full name',validators = [DataRequired()])
    awards = TextAreaField('Write your Blog ',validators=[DataRequired()])
    experience = TextAreaField('Write your Blog ',validators=[DataRequired()])


    submit = SubmitField('Post')

