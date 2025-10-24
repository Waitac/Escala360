from . import db

class Plantao(db.Model):
    __tablename__ = 'plantoes'
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date, nullable=False)
    hora_inicio = db.Column(db.Time, nullable=False)
    hora_fim = db.Column(db.Time, nullable=False)
    id_funcao = db.Column(db.Integer, nullable=False)
    id_local = db.Column(db.Integer, nullable=False)

    escalas = db.relationship('Escala', back_populates='plantao', lazy=True)