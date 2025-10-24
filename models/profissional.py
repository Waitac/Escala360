from flask_login import UserMixin
from . import db

class Profissional(UserMixin, db.Model):
    __tablename__ = 'profissionais'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    cargo = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    telefone = db.Column(db.String)
    ativo = db.Column(db.Boolean, default=True)

    escalas = db.relationship('Escala', back_populates='profissional', lazy=True)