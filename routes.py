from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user
from projeto import app, db, lm
from projeto.models.funcionario import User
from projeto.forms import LoginForm
from projeto.models.admin import Admin



@lm.user_loader
def load_user(id):
    return Admin.query.filter_by(id=id).first()

#função pronta
@app.route('/', methods=['GET', 'POST'])
def home():
    db.create_all()
    form = LoginForm()
    if form.validate_on_submit():
        admin = Admin.query.filter_by(usuario=form.usuario.data).first()
        if admin and admin.senha == form.senha.data:
            login_user(admin)
            return redirect(url_for("index"))

    return render_template('login.html', form=form)

#incompleta
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('home.html')


#função pronta
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        telefone = request.form['telefone']
        cod_registro = request.form['cod_registro']

        user = User(name, email, telefone, cod_registro)
        db.session.add(user)
        db.session.commit()

    return render_template('cadastro.html')

#falta implementar a visualização dos funcionarios
@app.route('/exibir', methods=['GET', 'POST'])
def exibir():
    FuncionarioData = User.query.all()
    return render_template('exibir.html', FuncionarioData=FuncionarioData)



#função pronta
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("home"))


app.run(debug=True)