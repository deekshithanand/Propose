from flask_wtf import FlaskForm
from wtforms import validators,StringField,TextAreaField

class PostForm(FlaskForm):
    name = StringField("Proposal Title",[validators.DataRequired()])
    description = TextAreaField("Elaborate Your Proposal",[validators.DataRequired()])
    