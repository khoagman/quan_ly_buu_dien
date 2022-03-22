from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired

class TestForm(FlaskForm):
    num = IntegerField(label='Number:', validators=[DataRequired()])
    submit = SubmitField(label='Xac nhan')
