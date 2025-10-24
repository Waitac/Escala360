from . import db

class Escala(db.Model):
    __tablename__ = 'escalas'
    id = db.Column(db.Integer, primary_key=True)
    id_plantao = db.Column(db.Integer, db.ForeignKey('plantoes.id'), nullable=False)
    id_profissional = db.Column(db.Integer, db.ForeignKey('profissionais.id'), nullable=False)
    status = db.Column(db.String, default='ativo')
    data_alocacao = db.Column(db.DateTime)

    plantao = db.relationship('Plantao', back_populates='escalas', lazy=True)
    profissional = db.relationship('Profissional', back_populates='escalas', lazy=True)
