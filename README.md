🏥 Escala360

Sistema web para gestão de escalas de profissionais da saúde em ambiente hospitalar, com recursos de alocação de plantões, substituição automatizada, dashboard com gráficos e controle de carga horária.
📋 Funcionalidades
✅ Gestão de Profissionais e PlantõesCadastro de profissionais (médicos, enfermeiros, técnicos)
Criação e visualização de plantões,
Alocação automática com validação de conflitos

📊 Dashboard InterativoCards com totais de profissionais, plantões ativos e substituições pendentesGráficos dinâmicos (barras, pizza e linha)Filtros por ano e mêsVisualização em tempo real

🔄 Sistema de SubstituiçõesMarcação de plantões como "pendente"Sugestão automática de substitutos disponíveisValidação de conflito de horárioControle de carga horária máxima🔐 Autenticação e SegurançaSistema de login com Flask-LoginSenhas criptografadas com bcryptSessões seguras🛠 TecnologiasBackend: Python 3.11, Flask, Flask-Login, SQLAlchemyFrontend: HTML5, CSS3, JavaScript, Chart.jsBanco de Dados: PostgreSQL 15Containerização: Docker, Docker ComposeServidor Web: Gunicorn (produção)🚀 Instalação e ExecuçãoPré-requisitosDockerDocker ComposePasso a passoClone o repositório:git clone https://github.com/seuusuario/escala360.git
cd escala360Configure as variáveis de ambiente:Crie um arquivo .env na raiz do projeto:FLASK_APP=app.py
FLASK_ENV=production
SECRET_KEY=sua-chave-secreta-aqui
DATABASE_URL=postgresql://escala360:senha123@db:5432/escala360Suba os containers:docker-compose up -dExecute as migrações do banco de dados:docker-compose exec web flask db upgradePopule o banco com dados iniciais (opcional):docker-compose exec web flask shellDentro do shell, execute:from models import db
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

exit()Acesse a aplicação:Abra o navegador em: http://localhost:5000Usuário: admin@escala360.comSenha: senha123📂 Estrutura do Projetoescala360/
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
    └── BPMN.md🐳 Comandos Docker ÚteisVer logs da aplicação:docker-compose logs -f webAcessar o container:docker-compose exec web bashReiniciar containers:docker-compose restartParar containers:docker-compose downReconstruir imagens:docker-compose up -d --buildBackup do banco de dados:docker-compose exec db pg_dump -U escala360 escala360 > backup.sqlRestaurar backup:cat backup.sql | docker-compose exec -T db psql -U escala360 escala360📖 DocumentaçãoRegras de NegócioDocumento de RequisitosCasos de UsoBanco de DadosConsultas SQL úteisModelo de dadosProcessosDiagrama BPMNFluxo de substituiçãoAlgoritmosLógica de sugestão de substitutos🧪 TestesExecutar testes unitários:docker-compose exec web pytestExecutar com cobertura:docker-compose exec web pytest --cov=.🔧 DesenvolvimentoModo de desenvolvimento com hot-reload:Altere o docker-compose.yml:environment:
  - FLASK_ENV=development
volumes:
  - .:/appDepois reinicie:docker-compose down
docker-compose up -d📊 Endpoints da APIDashboardGET /dashboard - Visualização do dashboardGET /api/available-periods - Retorna anos/meses com plantõesGET /api/dashboard-data?ano=2025&mes=7 - Dados para gráficosEscalasGET /escalas - Lista todas as escalasGET /escalas/<id>/substituir - Tela de substituiçãoPOST /escalas/<id>/substituir - Confirma substituiçãoAutenticaçãoGET /login - Tela de loginPOST /login - Efetua loginGET /logout - Efetua logout🛡️ SegurançaSenhas armazenadas com hash bcryptProteção contra CSRFSessões com timeout configurávelValidação de entrada em todos os formuláriosProteção contra SQL Injection via SQLAlchemy ORM🤝 ContribuindoFork o projetoCrie uma branch para sua feature (git checkout -b feature/MinhaFeature)Commit suas mudanças (git commit -m 'Adiciona MinhaFeature')Push para a branch (git push origin feature/MinhaFeature)Abra um Pull Request📝 LicençaEste projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.👥 AutoresSeu Nome - Desenvolvedor Principal - GitHub📞 SuportePara reportar bugs ou sugerir melhorias, abra uma issue.Desenvolvido com ❤️ para otimizar a gestão hospitalarEste README está completo com instruções para Docker, comandos úteis, estrutura do projeto e documentação. Quer adicionar mais alguma seção específica?