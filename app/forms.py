from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, TextAreaField
import re
from wtforms.validators import  DataRequired
from .models import Users, News
class RegistrationForm(FlaskForm):
    username=StringField(validators=[DataRequired(message="Обязательно к заполнению")])
    password=PasswordField(validators=[DataRequired(message="Обязательно к заполнению")])
    submit=SubmitField("Зарегестрироваться")


class LoginForm(FlaskForm):
    username=StringField(validators=[DataRequired(message="Обязательно к заполнению")])
    password=PasswordField(validators=[DataRequired(message="Обязательно к заполнению")])
    submit=SubmitField("Войти")
class PostsForm(FlaskForm):
    id=IntegerField()
    name_post=StringField()
    text_post=TextAreaField()
    url=StringField()
    submit=SubmitField("Добавить новость")
def replace_img_src(text):
    # Регулярное выражение для поиска тегов <img>
    img_pattern = re.compile(r'<img\s+src="images/([^"]+)/image\.png"([^>]*)>')

    # Функция для замены пути к изображению
    def replace_src(match):
        url = match.group(1)
        additional_attrs = match.group(2)
        new_src = f'src="{{url_for(\'static\', \'images/{url}/image.png\')}}'
        return f'<img {new_src} {additional_attrs}>'

    # Замена всех вхождений тегов <img>
    new_text = img_pattern.sub(replace_src, text)

    return new_text