from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from models.escala import Escala
from models.profissional import Profissional
from models.plantao import Plantao
from models import db

escala_blueprint = Blueprint('escala', __name__)

@escala_blueprint.route('/escalas')
@login_required
def mostrar_escalas():
    filtros = {}
    if 'status' in request.args:
        filtros['status'] = request.args.get('status')
    # Pode receber filtros via query string, por exemplo ?status=ativo
    escalas = Escala.query.filter_by(**filtros).all()
    return render_template('escalas.html', escalas=escalas)

@escala_blueprint.route('/escalas/alterar-status/<int:escala_id>', methods=['POST'])
@login_required
def alterar_status(escala_id):
    escala = Escala.query.get_or_404(escala_id)
    novo_status = request.form.get('status')
    if novo_status:
        escala.status = novo_status
        db.session.commit()
        flash('Status alterado com sucesso')
    else:
        flash('Status inválido')
    return redirect(url_for('escala.mostrar_escalas'))


@escala_blueprint.route('/escalas/substituir/<int:escala_id>', methods=['GET', 'POST'])
@login_required
def substituir_profissional(escala_id):
    escala = Escala.query.get_or_404(escala_id)

    if request.method == 'POST':
        substituto_id = request.form.get('substituto_id')
        substitutos_validos = [p.id for p in sugerir_substitutos(escala)]
        if substituto_id and int(substituto_id) in substitutos_validos:
            escala.id_profissional = int(substituto_id)
            escala.status = 'substituido'
            db.session.commit()
            flash('Substituição realizada com sucesso.')
            return redirect(url_for('escala.mostrar_escalas'))
        else:
            flash('Substituto inválido ou indisponível.')

    substitutos = sugerir_substitutos(escala)
    return render_template('substituir.html', escala=escala, substitutos=substitutos)


def sugerir_substitutos(escala):
    # Extrair dados do plantão e cargo atual
    cargo = escala.profissional.cargo
    plantao = escala.plantao
    data = plantao.data
    hora_inicio = plantao.hora_inicio
    hora_fim = plantao.hora_fim

    # Buscar profissionais que possuem o mesmo cargo e estão ativos
    candidatos = Profissional.query.filter(
        Profissional.cargo == cargo,
        Profissional.ativo == True,
        # Filtrar profissionais que não têm outro plantão ativo em conflito de horário
        ~Profissional.escalas.any(
            (Escala.plantao.has(Plantao.data == data)) &
            (Escala.plantao.has(Plantao.hora_inicio < hora_fim)) &
            (Escala.plantao.has(Plantao.hora_fim > hora_inicio)) &
            (Escala.status == 'ativo')
        )
    ).order_by(Profissional.nome).all()

    # Aqui você pode adicionar regras adicionais:
    # - Buscar profissionais com cargos similares se candidatos estiverem vazios
    # - Ordenar candidatos por preferências, histórico, proximidade etc.

    return candidatos
