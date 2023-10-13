# alura-sapece

# Instalando o Django
## Instale o venv
    - virtualenv venv
## Ative o venv
    Escreva no terminal o seguinte comando:
    - venv\Scripts\Activate
    * Para desativar basta escrever "deactivate"
## Instale o Django dentro do ambiente virtual
    - pip install django
## Instalando os requerimentos
    - pip freeze > requirements.txt
    - pip install 
## Criando projeto no django
    -django-admin startproject setup .
## Iniciando servidor
    - python manage.py runserver

# Escondendo SECRET_KEY
    - pip install python-dotenv
    - pip freeze > requirements.txt
    - criar um arquivo .env e copiar o SECRET_KEY
    - Importar da pathlib a blibloteca 'os'  e da biblioteca dotenv o 'load_dotenv' no settings.py
    - Inserir no settings.py a função load_dotenv()
    - Inserir no SECRET_KEY a variável 'str(os.getenv('SECRET_KEY'))'
    - iniciar o servidor: python manage.py runserver
# Criando .gitignore
    - Entrar no site gitignore.io
    - Copiar o codigo para o django
    