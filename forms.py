from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import PasswordField
from wtforms.validators import DataRequired, EqualTo
from models import User #Models.py 가져옴

class RegisterForm(FlaskForm):
    userid = StringField('userid', validators=[DataRequired()])
    #email = StringField('email', validators=[DataRequired()])
    #password = PasswordField('password', validators=[DataRequired(), EqualTo('password_2')]) #비밀번호 확인
    #password_2 = PasswordField('password_2', validators=[DataRequired()])

class LoginForm(FlaskForm):


    userid = StringField('AxieID', validators=[DataRequired()])
    #class UserPassword(object):
    def __init__(self, message=None):
        self.message = message
        super(LoginForm,self).__init__()
            
    def __call__(self, form, _fields):
        userid = form['userid'].data
            #password = field.data
            
        usertable = User.query.filter_by(userid=userid).first()
            #usertable = User.query.filter_by(password=password).first()

            #if usertable.password!= password:
            #    raise ValueError('Wrong password')
    

        userid = StringField('userid', validators=[DataRequired()])
    #password = PasswordField('password', validators=[DataRequired(), UserPassword()])