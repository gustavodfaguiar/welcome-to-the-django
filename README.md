# Eventex 

Projeto do curso Welcome to the Django

[![Build Status](https://travis-ci.org/gusttavoaguiarr/welcome-to-the-django.svg?branch=master)](https://travis-ci.org/gusttavoaguiarr/welcome-to-the-django)
[![Code Health](https://landscape.io/github/gusttavoaguiarr/welcome-to-the-django/master/landscape.svg?style=flat)](https://landscape.io/github/gusttavoaguiarr/welcome-to-the-django/master)
[![Ebert](https://ebertapp.io/github/gusttavoaguiarr/welcome-to-the-django.svg)](https://ebertapp.io/github/gusttavoaguiarr/welcome-to-the-django)
[![Coverage Status](https://coveralls.io/repos/github/gusttavoaguiarr/welcome-to-the-django/badge.svg?branch=master)](https://coveralls.io/github/gusttavoaguiarr/welcome-to-the-django?branch=master)


## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.5
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env
6. Execute os testes.

```console
git clone https://github.com/gusttavoaguiarr/welcome-to-the-django welcome-to-the-django
cd welcome-to-the-django
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy?

1. Crie uma instância no heroku.
2. Envie as configurações para o heroku.
3. Defina uma SECRET_KEY segura para instância.
4. Defina DEBUG=False
5. Configure o serviço de e-mail
6. Envie o código para o heroku.

```console
heroku create minha-instancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# configuro o e-mail
git push heroku master --force
```
