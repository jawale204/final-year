from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo,ValidationError
from flaskblog.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')



class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class ParametersForm(FlaskForm):
    Id=StringField('id',
                        validators=[DataRequired()])
    hour=StringField('hour',
                        validators=[DataRequired()])
    site_id=StringField('site_id',
                        validators=[DataRequired()])
    app_id=StringField('app_id',
                        validators=[DataRequired()])
    app_domain=StringField('app_domain',
                        validators=[DataRequired()])
    site_domain=StringField('site_domain',
                        validators=[DataRequired()])
    site_category=StringField('site_category',
                        validators=[DataRequired()])
    device_id=StringField('device_id',
                        validators=[DataRequired()])
    device_ip=StringField('device_ip',
                        validators=[DataRequired()])
    device_type=StringField('device_type',
                        validators=[DataRequired()])
    device_model=StringField('device_model',
                        validators=[DataRequired()])
    '''C14=StringField('C14',
                        validators=[DataRequired()])
    C15=StringField('C15',
                        validators=[DataRequired()])
    C16=StringField('C16',
                        validators=[DataRequired()])
    C17=StringField('C17',
                        validators=[DataRequired()])
    C18=StringField('C18',
                        validators=[DataRequired()])
    C19=StringField('C19',
                        validators=[DataRequired()])
    C20=StringField('C20',
                        validators=[DataRequired()])'''
    submit=SubmitField('submit')
        