from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateTimeField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class CadastroForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    telefone = StringField('Telefone', validators=[DataRequired()])
    endereco_barbearia = StringField('Endereço da Barbearia', validators=[DataRequired()])
    nome_barbearia = StringField('Nome da Barbearia', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Cadastrar')

class CriarHorarioForm(FlaskForm):
    data_hora = StringField('Data e Hora', validators=[DataRequired()])  
    submit = SubmitField('Criar Horário')

class AgendarHorarioForm(FlaskForm):
    nome_cliente = StringField('Seu Nome', validators=[DataRequired()]) 
    submit = SubmitField('Confirmar Agendamento')
