# Use imagem oficial Python
FROM python:3.11-slim

# Define diretório de trabalho
WORKDIR /app

# Copia requirements.txt e instala dependências
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código da aplicação
COPY . .

# Expõe a porta 5000 para Flask
EXPOSE 5000

# Variável de ambiente para evitar buffer no output
ENV PYTHONUNBUFFERED=1

# Comando para rodar o app
CMD ["flask", "run", "--host=0.0.0.0"]
