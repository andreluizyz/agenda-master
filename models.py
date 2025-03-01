from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    agendamentos = db.relationship('Agendamento', backref='cliente', lazy=True) 

class Profissional(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    agendamentos = db.relationship('Agendamento', backref='profissional', lazy=True)  

class Agendamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_hora = db.Column(db.String(50), nullable=False)
    nome_profissional = db.Column(db.String(100), nullable=False)  
    profissional_id = db.Column(db.Integer, db.ForeignKey('profissional.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True) 
    nome_cliente = db.Column(db.String(100), nullable=True)  
    disponivel = db.Column(db.Boolean, default=True) 
