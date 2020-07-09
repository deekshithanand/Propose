from flask_wtf import FlaskForm
from wtforms import StringField,validators,SubmitField,TextAreaField

class TopicForm(FlaskForm):
    topic_name = StringField('Topic Name',
    [validators.DataRequired()]
    )
    topic_description = TextAreaField('Topic Description')
    