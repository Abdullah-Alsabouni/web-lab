from app import app
from flask import render_template
from app.forms import LoginForm
from flask import render_template, flash, redirect

@app.route('/') # @app bir dekoratör, bu fonksiyonun hangi URL'ye yanıt vereceğini belirtir
@app.route('/index')
def index():
    user = {'username': 'Abdullah'} # Örnek kullanıcı verisi
    posts = [ # Örnek blog gönderileri
        {
            'author': {'username': 'Abdullah'},
            'body': 'Beautiful day in Samsun!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts = posts) # HTML şablonunu render eder
@app.route('/about')  # Yeni "About" sayfası için rota
def about():
    return render_template('about.html', title='About')  # Yeni şablon dosyasını render et

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)