from . import db

class Substituicao(db.Model):
    __tablename__ = 'substituicoes'
    id = db.Column(db.Integer, primary_key=True)
    id_escala_original = db.Column(db.Integer, db.ForeignKey('escalas.id'), nullable=False)
    id_profissional_solicitante = db.Column(db.Integer, db.ForeignKey('profissionais.id'), nullable=False)
    id_profissional_substituto = db.Column(db.Integer, db.ForeignKey('profissionais.id'), nullable=False)
    data_solicitacao = db.Column(db.DateTime)
    status = db.Column(db.String, default='pendente')
