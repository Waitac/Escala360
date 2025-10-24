from . import db

class Auditoria(db.Model):
    __tablename__ = 'auditoria'
    id = db.Column(db.Integer, primary_key=True)
    entidade = db.Column(db.String, nullable=False)
    id_entidade = db.Column(db.Integer, nullable=False)
    acao = db.Column(db.String, nullable=False)
    usuario = db.Column(db.String, nullable=False)
    data_hora = db.Column(db.DateTime)
