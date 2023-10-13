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
# Criando novo app
    - Com o ambiente do django ativado digitar:
        python manage.py startapp nomedoapp
    - No arquivo settings.py adicionar o app criado em INSTALLED_APPS
        ...
        'nomedoapp',
        ...
# Exibindo app criado
    - Em galeria > views importar a biblioteca:
        from django.http from HttpResponse
    - Criar função:
        def index(request):
            return HttpResponde('<h1>Alura-Space</h1>')
    - Importar no arquivo em setup/urls.py:
        from galeria.views import index
    - Configurar dentro do array 'urlpatterns'
        path('', index),

# Organizando arquivo de rotas de apps
    - Criar dentro da pasta do app o arquivo 'urls.py'
    - importar o método path do django.urls
    - importar o método index da galeria.views
        from galeria.views import index
    - Adicionar a lista de paths:
        urlpatterns = [
            path('', index)
        ]
    - Na pasta setup > urls.py adicionar o método include:
        from django.urls import path, include
    - Dentro do urlpatterns alterar index por include
        urlpatterns = [
            path('', include('galeria.urls'))
        ]
# Criando os templates
    - Criar dentro da pasta principal uma pasta templates
    - Na pasta setup > settings.py na linha de TEMPLATES adicionar:
        'DIRS': [os.path.join(BASE_DIR, 'templates')]

# Criando HTML
    - Criar na pasta template o index.html
    - Apertar o botão '!' para que o html seja escrito automaticamente.
    - Criar em <body> uma tag <h1>Teste</h1>:
        <body>
            <h1>Teste</h1>
        </body>
    - Em galeria > views alterar o HttpRequest para render:
        def index(request):
            return render(request, 'index.html') 
    - Deletar o import do HttpResponse

# Carregando Front-End HTML e CSS
    - copiar o frontend dado pela alura e copiar em index.html
    - Em setup criar a pasta static
    - Criar dentro da pasta static as pastas assets e styles
    - Em settings.py criar o seguinte caminho de pasta:
        STATICFILES_URL = [
            os.path.join(BASE_DIR, 'SETUP/static')
        ]
        STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    - utilizar o comando para coleta de dados estáticos:
        python manage.py collectstatic
    - Dentro do index.html em templates\galeria adicionar o seguinte código:
        {% load static %}
        ...
        <head>
            ...
             <link rel="stylesheet" href="{% static '/styles/style.css' %}">
        </head>
    - Em todos os arquivos estáticos <img src=""> colocar a tag {%Static ''%}

# Ir para outra página quando clicar
    - Criar na pasta templates/galeria o arquivo imagem.html