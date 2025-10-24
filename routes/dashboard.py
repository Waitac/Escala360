from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required
from models.profissional import Profissional
from models.escala import Escala
from models.plantao import Plantao
from models.substituicao import Substituicao
from datetime import datetime
from sqlalchemy import extract
from models import db

dashboard_blueprint = Blueprint('dashboard', __name__)

@dashboard_blueprint.route('/dashboard')
@login_required
def dashboard():
    total_profissionais = Profissional.query.count()
    plantoes_ativos = Escala.query.filter_by(status='ativo').count()
    substituicoes_pendentes = Escala.query.filter_by(status='pendente').count()  # ALTERADO
    return render_template(
        'dashboard.html',
        total_profissionais=total_profissionais,
        plantoes_ativos=plantoes_ativos,
        substituicoes_pendentes=substituicoes_pendentes
    )

@dashboard_blueprint.route('/api/available-periods')
@login_required
def available_periods():
    plantoes = Plantao.query.with_entities(Plantao.data).all()
    periodos = set()
    for (data,) in plantoes:
        if data:
            periodos.add((data.year, data.month))
    periodos_ord = sorted(list(periodos))
    return jsonify([{"ano": ano, "mes": mes} for (ano, mes) in periodos_ord])


@dashboard_blueprint.route('/api/dashboard-data')
@login_required
def dashboard_data():
    try:
        ano = int(request.args.get('ano'))
        mes_num = int(request.args.get('mes'))
        inicio_mes = datetime(ano, mes_num, 1)
        if mes_num == 12:
            fim_mes = datetime(ano + 1, 1, 1)
        else:
            fim_mes = datetime(ano, mes_num + 1, 1)
    except Exception:
        return jsonify({"error": "Parâmetros de ano e mês são obrigatórios e válidos"}), 400

    plantoes_mes = Escala.query.join(Escala.plantao).filter(
        Plantao.data >= inicio_mes,
        Plantao.data < fim_mes
    ).all()

    plantoes_semana = [0, 0, 0, 0]
    for escala in plantoes_mes:
        dia = escala.plantao.data.day
        if dia <= 7:
            plantoes_semana[0] += 1
        elif dia <= 14:
            plantoes_semana[1] += 1
        elif dia <= 21:
            plantoes_semana[2] += 1
        else:
            plantoes_semana[3] += 1

    cargos_count = {}
    for escala in plantoes_mes:
        cargo = escala.profissional.cargo
        cargos_count[cargo] = cargos_count.get(cargo, 0) + 1

    pizzas_labels = list(cargos_count.keys())
    pizzas_data = list(cargos_count.values())

    substituicoes_dia = {}
    for escala in plantoes_mes:
        if escala.status == 'substituido' and getattr(escala, 'data_alocacao', None):
            dia = escala.data_alocacao.day
            substituicoes_dia[dia] = substituicoes_dia.get(dia, 0) + 1

    linha_labels = [str(i) for i in range(1, 32)]
    linha_data = [substituicoes_dia.get(i, 0) for i in range(1, 32)]

    return jsonify({
        "barra": {
            "labels": ["Semana 1", "Semana 2", "Semana 3", "Semana 4"],
            "data": plantoes_semana
        },
        "pizza": {
            "labels": pizzas_labels,
            "data": pizzas_data
        },
        "linha": {
            "labels": linha_labels,
            "data": linha_data
        }
    })
