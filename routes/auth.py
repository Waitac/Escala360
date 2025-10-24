from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required
from models.profissional import Profissional
from models import db

auth_blueprint = Blueprint('auth', __name__)

# Redireciona a raiz para a tela de login
@auth_blueprint.route('/')
def root():
    return redirect(url_for('auth.login'))

@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email', '')
        senha = request.form.get('senha', '')
        print(f"Login tentado com email: {email} e senha: {senha}")
        usuario = Profissional.query.filter_by(email=email).first()
        if usuario:
            print(f"Usuário encontrado: {usuario.nome}")
            login_user(usuario)
            return redirect(url_for('escala.mostrar_escalas'))
        else:
            print("Usuário não encontrado")
        flash('Usuário ou senha inválidos')
    return render_template('login.html')

@auth_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
