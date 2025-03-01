from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, login_user, login_required, current_user, logout_user
from models import db, User, Agendamento, Profissional
from flask_migrate import Migrate
from config import Config
from forms import LoginForm, CadastroForm, CriarHorarioForm, AgendarHorarioForm 
import os


app = Flask(__name__)
app.config.from_object(Config) 
db.init_app(app) 


login_manager = LoginManager(app)
login_manager.login_view = 'login'


migrate = Migrate(app, db)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


with app.app_context():
    db.create_all()


@app.route('/')
def index():
    agendamentos = Agendamento.query.filter_by(disponivel=True).all() 
    return render_template('index.html', agendamentos=agendamentos)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data: 
            login_user(user)
            return redirect(url_for('dashboard'))
        flash('Usuário ou senha incorretos!', 'danger')
    return render_template('login.html', form=form)

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    form = CadastroForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Usuário cadastrado com sucesso!', 'success')
        return redirect(url_for('login'))
    return render_template('cadastro.html', form=form)

@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    form = CriarHorarioForm()  
    if form.validate_on_submit():
        agendamento = Agendamento(
            data_hora=form.data_hora.data,
            profissional_id=current_user.id, 
            nome_profissional=current_user.username,  
            disponivel=True
        )
        db.session.add(agendamento)
        db.session.commit()
        flash('Horário cadastrado com sucesso!', 'success')
        return redirect(url_for('dashboard'))

   
    agendamentos = Agendamento.query.filter_by(profissional_id=current_user.id).all()
    return render_template('dashboard.html', form=form, agendamentos=agendamentos)

@app.route('/agendar/<int:agendamento_id>', methods=['GET', 'POST'])
def agendar_horario(agendamento_id):
    agendamento = Agendamento.query.get_or_404(agendamento_id)
    form = AgendarHorarioForm()
    if request.method == 'POST':
        nome_cliente = request.form.get('nome_cliente')
        
        if nome_cliente and agendamento.disponivel:
            agendamento.nome_cliente = nome_cliente
            agendamento.disponivel = False  
            db.session.commit()
            flash('Agendamento realizado com sucesso!', 'success')
            return redirect(url_for('index'), ) 

    return render_template('agendar.html', agendamento=agendamento, form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))  # Pega a variável de ambiente PORT ou usa 5000 por padrão
    app.run(host='0.0.0.0', port=port)  # Escuta em 0.0.0.0 e na porta fornecida pelo Render
