
import sqlite3
from flask import Flask, url_for, redirect, render_template
from flask_login import LoginManager, login_user, login_required, logout_user
import re
from . import app, users, bcrypt
from .forms import RegistrationForm, LoginForm, PostsForm
from .models import News, Users
from markupsafe import Markup
login_manager = LoginManager(app)
login_manager.login_view = "login"
@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))
def get_title_post(alias):
    try:
        conn = sqlite3.connect('users.sqlite3')
        cursor = conn.cursor()
        cursor.execute(f"SELECT name, text_news FROM news WHERE url LIKE ? LIMIT 1", (alias,))
        res = cursor.fetchone()
        if res:
            base = url_for('static', filename='images')
            text = re.sub(r"(?P<tag><img\s+[^>]*src=)(?P<quote>[\"'])(?P<url>.+?)(?P=quote)>",
                          "\\g<tag>" + base + "/\\g<url>>",
                          res[1])
            print(res[1])
            print('\n\n')
            print(text)

            return (res[0], text)

    except sqlite3.Error as e:
        print("Ошибка при получении статьи"+str(e))
    return (False, False)

# def get_strok(content):
#     pattern=r'<img\s+[^>]*>'
#     pattern_name=r'<img\s+[^>]*src=["\']([^"\']+)["\'][^>]*>'
#     name_with_url=''
#     strok=''
#
#     news_content=re.findall(pattern, content)
#     names=[]
#     print(news_content)
#     for i in news_content:
#         n=re.findall(pattern_name, i)
#         names.append(*n)
#         for i in names:
#             name=str(i)
#             news_way = f'<img src="{{{{url_for(\'static\', filename='/'.join(['imges', 'name', profilePic]))}}}} class="img-fluid" align="center">"'
#             strok = news_way
#     new_content=re.sub(pattern, strok, content)
#     return new_content


@app.route('/dashboard', methods=['GET','POST'])
@login_required
def dashboard():
    return render_template('dashboard.html')
@app.route('/news', methods=['GET','POST'])
def news():
    news_list=News.query.all()
    return render_template('news.html', news=news_list)
@app.route('/news_more/<alias>', methods=['GET','POST'])
def news_more(alias):
    title, post=get_title_post(alias)
    t=Markup(title)
    p=Markup(post)
    return render_template('news_more.html', title=t, post=p)
@app.route('/', methods=['GET','POST'])
def index():
    print("I am ok")
    return render_template('index.html')
@app.route('/add_news', methods=['GET','POST'])
@login_required
def add_news():
    form=PostsForm()
    if form.validate_on_submit():
        news=News()
        news.name=form.name_post.data
        news.url=form.url.data
        text=form.text_post.data
        news.text_news=text
        users.session.add(news)
        users.session.commit()
        return redirect(url_for('news_more', alias=news.url))
    return render_template('add_news.html', form=form)
@app.route('/login', methods=['GET','POST'])
def login():
    form=LoginForm()

    if form.validate_on_submit():
        user=Users.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
            return redirect('dashboard')
    return render_template('login.html', form=form)
@app.route('/register', methods=['GET','POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        hashed_password=bcrypt.generate_password_hash(form.password.data)
        new_user=Users(username=form.username.data, password=hashed_password)
        users.session.add(new_user)
        users.session.commit()
        return redirect(url_for('login'))

    return render_template('register.html', form=form)
@app.route('/logout/')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
@app.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():
    return render_template('admin.html')
@app.route('/kiwi_page', methods=['GET', 'POST'])
def kiwi_page():
    return render_template('kiwi_page.html')
