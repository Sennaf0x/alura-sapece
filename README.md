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
    - Configurar em views.py a rota para renderizar o imagem.html
        def index(request):
            return render(request, 'galeria/imagem.html')
    - Configurar em galeria > urls.py a nova rota:
        ...
        from galeria.views import index, imagem
        ...
            urlpatterns = [
                ...
                path('imagem/', imagem, name = 'imagem')
            ]   
        ...
    -Adicionar no imagem.html a função do python {% url 'imagem'%} em todos as ancoras que redicecionam para a pagina index:
        Antes: <a href="imagem.html">
        Depois <a href= "{% url 'imagem' %}">
# Tornando o app menos repetivivo
    - Criar um arquivo chamado base.html e copiar toda parte de <head> do index html.
    - Apagar o <head>, <body> e <html> do index.html e imagem.html
    - Nos respectivos arquivos html escrever {% extends 'galeria/base.html' %}, {% block content %} e {% endblock %}
    - Adicionar no arquivo base.html o {% block content %} e {% endblock %} no <body>:
        ...
        <body>
        {% block content %}{% endblock %}
        </body>
        ...
# Criando partials
    - Crie uma pasta em template\galeria chamado partials
    - Crie um arquivo html com "_" na frente por convenção, exemplo: 
        _footer.html
    - Copie toda a informação da parte do código que você quer que permaneça na página

# Estrutura de dados
    - Criar estrutura de dados em galeria > views dentro do def index:

    ...
    def index(request):

    **dados = {
        1: {"nome": "Nebulosa de Úrsula",
            "legenda": "webbtelescope.org / NASA / James Webb"},
        2: {"nome": "Galáxia NGC 1079",
            "legenda": "nasa.org / NASA / Hubble"}
        }**
    
        return render(request, 'galeria/index.html', **{"cards": dados}**)
    ...

# Criando um for 
    - No index.html adicionar antes da <li> lista de repetição o código e os locais onde aparecerão os dados {{ info.dados}}:
        ...
        <div class="cards">
                        <h2 class="cards__titulo">Navegue pela galeria</h2>
                        <ul class="cards__lista">
                        **{% for foto_id, info in cards.items %}**
                            <li class="card">
                        ...
                            <div class="card__info">
                                    <p class="card__titulo">**{{ info.nome }}**</p>
                                    <div class="card__texto">
                                        <p class="card__descricao">**{{ info.legenda }}**</p>
                                        <span>    
                        ...
                            </li>
                        **{% endfor%}** 

# Vinculando o for com o banco de dados
    - Criar na pasta galeria\models.py um classe chamada Fotografia e adicionar uma função que devolva o valor dos items:
    
        class Fotografia(models.Model):
            nome = models.CharField(max_Length = 100, null = False, blank = False)
            legenda = models.CharField(max_Length = 150, null = False, blank = False)
            descricao = models.TextField(null = False, blank = False)
            foto = models.CharField(max_Length = 150, null = False, blank = False)
    
        def __str__(self):
            return f"Fotografia[nome={self.nome}]"
    
    - executar o comando pyhton manage.py makemigrations
    - executar o comando pyhton manage.py migrate
    - instalar a a extensão sqlite viewer
    - Verificar se o banco de dados foi criado.

# Inserindo dados com o shell
    - Executar o comando python manage.py shell
    - importe a galeria.models
        from galeria.models import Fotografia
    - crie um novo dado:
        foto = Fotografia(nome ="Nebulosa de Úrsula", legenda ="webbtelescope.org / NASA / James Webb",foto = "carina-foto.png)
    - salve o dado:
        foto.save()
# Importando dados do shell 
    - Em galeria > views.py substituir o dicionário pela classe fotografia:
        
        from django.shortcuts import render
        **from galeria.models import Fotografia**

        def index(request):
            **fotografias = Fotografia.objects.all()** 
            return render(request, 'galeria/index.html', {"cards": **fotografias**})

        def imagem(request):
            return render(request, 'galeria/imagem.html')

    - Alterar no index.html o código do {% for %} e inserir um {% if %}
        <ul class="cards__lista">
                            **{% if cards%}**
                            {% for **fotografia** in **cards** %}
                            <li class="card">
                            ...
                            {% else %}
                            {% endif %}
    - Alterar info.nome  por fotografia.nome, info.legenda por fotografia legenda
    - Adicionar no src da imagem a seguinte chamada do banco de dados:
        
        <img class="card__imagem" src="{% static '/assets/imagens/galeria/'%}**{{ fotografia.foto }}**" alt="foto">
# Passando o id da imagem ao clicar na foto
    - Adicionar à referência {% url 'imagem' %} o valor do id:
        {% url 'imagem' fotografia_id%}
    - Adiciona ro valor do id na url da página de imagens em urls.py:
        path('imagem/<int:foto_id>', imagem, name='imagem'),
    - Adicionar no arquivo views.py no método que istancia as imagens o foto_id após o request:
        def imagem(request, foto_id):
    - Importar o método get_objects_or_404
        from django.shortcuts import render, **get_object_or_404**
    - Dentro do método que instancia a imagem passamos nossomodel e seu valor:
        fotografia = get_object_or_404(Fotografia, pk=foto_id)
    - É adicionado no return um dicionário com valor fotografia:
        return render(request, 'galeria/imagem.html', {"fotografia": fotografia})
    - Por fim, passar os valores de fotografia.nome, fotografia.foto e fotografia.legenda nos seus respectivos campos no imagem.html.

# Django admin, criando super usuario
    - Execute o comando python manage.py createsuperuser e adicione login e senha.
    - Entre no admin do django 127.0.0.1:8000/admin
# Criando CRUD no admin
    - Entre no arquivo galeria > admin.py e configurar o admin:
        from django.contrib import admin
        from galeria.models import Fotografia
    
        class ListandoFotografias(admin.ModelAdmin):
            list_display = ("id","nome", "legenda")
            list_displaylinks = ("id","nome")
            search_fields =("nome",)

    admin.site.register(Fotografia, ListandoFotografias)
# Criando categorias
    - Cria uma lista no models.py dentro da classe Fotografia
    

        OPCOES_CATEGORIA = [
            ("NEBULOSA"),
            ("ESTRELA"),
            ("GALÁXIA"),
            ("PLANETA")
        ]
    - Crie uma variável categoria com a seguinte configuração:
        categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='')
    - Atualize os models com o comando python manage.py makemigrations e python manage.py migrate