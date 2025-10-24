from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Importar todos os modelos para registro das tabelas
from .profissional import Profissional
from .plantao import Plantao
from .escala import Escala
from .substituicao import Substituicao
from .auditoria import Auditoria
