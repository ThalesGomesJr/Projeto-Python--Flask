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
            flash('Login realizado com sucesso', 'success')
            return redirect(url_for("index"))
        else:
            flash('Login Invalido', 'danger')
            return redirect(url_for("home"))

    return render_template('login.html', form=form)

#função pronta
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
        flash('Funcionario cadastrado com sucesso', 'success')

    return render_template('cadastro.html')

#falta implementar a visualização dos funcionarios
@app.route('/exibir', methods=['GET', 'POST'])
def exibir():
    FuncionarioData = User.query.all()
    return render_template('exibir.html', FuncionarioData=FuncionarioData)


@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        telefone = request.form['telefone']
        cod_registro = request.form['cod_registro']
        FuncionarioData = User.query.get(int(id))
        FuncionarioData.name = name
        FuncionarioData.email = email
        FuncionarioData.telefone = telefone
        FuncionarioData.cod_registro = cod_registro
        
        db.session.add(FuncionarioData)
        db.session.commit()
        flash('Dados do funcionario foram atualizados com sucesso', 'success')
        return redirect(url_for('exibir'))
    
    FuncionarioData = User.query.get(int(id))
    return render_template('editar.html', FuncionarioData=FuncionarioData)



@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    FuncionarioData = User.query.get(int(id))
    db.session.delete(FuncionarioData)
    db.session.commit()
    flash('Funcionario removido com sucesso', 'success')
    return redirect(url_for('exibir'))
    
#função pronta
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("home"))


app.run(debug=True)