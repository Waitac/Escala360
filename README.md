🏥 Escala360

Sistema web para gestão de escalas de profissionais da saúde em ambiente hospitalar, com recursos de alocação de plantões, substituição automatizada, dashboard com gráficos e controle de carga horária.

📋 Funcionalidades

✅ Gestão de Profissionais e Plantões
- Cadastro de profissionais (médicos, enfermeiros, técnicos)
- Criação e visualização de plantões,
- Alocação automática com validação de conflitos

📊 Dashboard Interativo
- Cards com totais de profissionais, plantões ativos e substituições pendentes
- Gráficos dinâmicos (barras, pizza e linha)
- Filtros por ano e mês
- Visualização em tempo real

🔄 Sistema de Substituições
- Marcação de plantões como "pendente"
- Sugestão automática de substitutos disponíveis
- Validação de conflito de horário
- Controle de carga horária máxima

🔐 Autenticação e Segurança
- Sistema de login com Flask-Login
- Senhas criptografadas com bcrypt
- Sessões seguras

🛠 Tecnologias
- Backend: Python 3.11, Flask, Flask-Login, SQLAlchemy
- Frontend: HTML5, CSS3, JavaScript, Chart.js
- Banco de Dados: PostgreSQL 15
- Containerização: Docker, Docker Compose
- Servidor Web: Gunicorn (produção)

🚀 Instalação e Execução
Pré-requisitos
- Docker
- Docker Compose

Passo a passo

1. Clone o repositório: git clone https://github.com/seuusuario/escala360.git
cd escala360

2. Configure as variáveis de ambiente:
   Crie um arquivo .env na raiz do projeto:
       FLASK_APP=app.py
       FLASK_ENV=production
       SECRET_KEY=sua-chave-secreta-aqui
       DATABASE_URL=postgresql://escala360:senha123@db:5432/escala360
   
3. Suba os containers:
    docker-compose up -d

4. Execute as migrações do banco de dados:
    docker-compose exec web flask db upgrade
   
5. Popule o banco com dados iniciais (opcional):
    docker-compose exec web flask shell

   Dentro do shell, execute:
    from models import db
    from models.profissional import Profissional
    from models.user import User
   
    # Criar usuário admin
    admin = User(email='admin@escala360.com', nome='Admin')
    admin.set_password('senha123')
    db.session.add(admin)
    db.session.commit()
    
    # Criar profissionais de exemplo
    prof1 = Profissional(nome='Dr. João Silva', cargo='Médico', email='joao@hospital.com')
    prof2 = Profissional(nome='Enf. Maria Santos', cargo='Enfermeiro', email='maria@hospital.com')
    db.session.add_all([prof1, prof2])
    db.session.commit()
    
    exit()

6. Acesse a aplicação:
Abra o navegador em: http://localhost:5000
-Usuário: admin@escala360.com
-Senha: senha123



📂 Estrutura do Projeto

escala360/
├── app.py                    # Ponto de entrada da aplicação
├── config.py                 # Configurações do Flask
├── docker-compose.yml        # Orquestração dos containers
├── Dockerfile                # Imagem Docker da aplicação
├── requirements.txt          # Dependências Python
├── .env                      # Variáveis de ambiente (não versionado)
├── .gitignore               # Arquivos ignorados pelo Git
│
├── models/                   # Modelos de dados (SQLAlchemy)
│   ├── __init__.py
│   ├── profissional.py
│   ├── plantao.py
│   ├── escala.py
│   ├── substituicao.py
│   └── user.py
│
├── routes/                   # Rotas/Blueprints Flask
│   ├── __init__.py
│   ├── auth.py              # Autenticação
│   ├── dashboard.py         # Dashboard e gráficos
│   └── escala.py            # Gestão de escalas
│
├── templates/                # Templates Jinja2
│   ├── base.html
│   ├── login.html
│   ├── dashboard.html
│   ├── escalas.html
│   └── substituir.html
│
├── static/                   # Arquivos estáticos
│   ├── css/
│   │   ├── login.css
│   │   ├── dashboard.css
│   │   ├── escalas.css
│   │   └── substituir.css
│   └── js/
│       └── dashboard.js
│
└── docs/                     # Documentação
    ├── REQUISITOS.md
    ├── SQL.md
    ├── PROTOTIPOS.md
    └── BPMN.md
    
    
🐳 Comandos Docker Úteis
Ver logs da aplicação:
    docker-compose logs -f web
Acessar o container:
    docker-compose exec web bash
Reiniciar containers:
    docker-compose restart
Parar containers:
    docker-compose down
Reconstruir imagens:
    docker-compose up -d --build
Backup do banco de dados:
    docker-compose exec db pg_dump -U escala360 escala360 > backup.sql
Restaurar backup:
    cat backup.sql | docker-compose exec -T db psql -U escala360 escala360


🧪 TestesExecutar testes unitários:
    docker-compose exec web pytest
Executar com cobertura:
    docker-compose exec web pytest --cov=.🔧 DesenvolvimentoModo de desenvolvimento com hot-reload:Altere o docker-compose.yml:environment:
  - FLASK_ENV=development
volumes:
  - .:/appDepois reinicie:docker-compose down
docker-compose up -d

🛡️ Segurança

- Senhas armazenadas com hash bcrypt
- Proteção contra CSRF
- Sessões com timeout configurável
- Validação de entrada em todos os formulários
- Proteção contra SQL Injection via SQLAlchemy ORM

🤝 Contribuindo

Fork o projeto
- Crie uma branch para sua feature (git checkout -b feature/MinhaFeature)
- Commit suas mudanças (git commit -m 'Adiciona MinhaFeature')
- Push para a branch (git push origin feature/MinhaFeature)
- Abra um Pull Request

👥 Autores

Waita Cavalcante Moura - Desenvolvedor Principal - [GitHub](https://github.com/Waitac)

📞 Suporte

Para reportar bugs ou sugerir melhorias, abra uma issue.
