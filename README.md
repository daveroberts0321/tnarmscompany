### TN Arms Co Store Site 20221101

Django based ecommerce site built on top of DjangoX for the user signup and accounts

Uses Django-unicorn for front-end functionality starting at Shopping cart



dependencies:
asgiref==3.5.2
beautifulsoup4==4.11.1
cachetools==4.2.4
certifi==2022.9.24
cffi==1.15.1
charset-normalizer==2.1.1
coverage==6.5.0
cryptography==38.0.1
decorator==4.4.2
defusedxml==0.7.1
Django==4.0.4
django-allauth==0.50.0
django-crispy-forms==1.14.0
django-debug-toolbar==3.2.4
django-extensions==3.2.1
django-model-utils==4.2.0
django-resized==1.0.2
django-unicorn==0.48.0
django-widget-tweaks==1.4.12
flake8==5.0.4
flake8-django==1.1.5
idna==3.4
isort==5.10.1
mccabe==0.7.0
oauthlib==3.2.2
orjson==3.8.1
Pillow==9.2.0
psycopg2-binary==2.9.3
pycodestyle==2.9.1
pycparser==2.21
pyflakes==2.5.0
PyJWT==2.6.0
python3-openid==3.2.0
requests==2.28.1
requests-oauthlib==1.3.1
shortuuid==1.0.9
soupsieve==2.3.2.post1
sqlparse==0.4.3
tzdata==2022.5
unicorn==2.0.1
urllib3==1.26.12
whitenoise==6.0.0
# isort and flake8 for styling and testing 



























> A batteries-included Django starter project. To learn more try the books [Django for Beginners](https://djangoforbeginners.com), [Django for APIs](https://djangoforapis.com), and [Django for Professionals](https://djangoforprofessionals.com).

## 🚀 Features

- Django 4.0 & Python 3.10
- Install via [Pip](https://pypi.org/project/pip/), [Pipenv](https://pypi.org/project/pipenv/), or [Docker](https://www.docker.com/)
- User log in/out, sign up, password reset via [django-allauth](https://github.com/pennersr/django-allauth)
- Static files configured with [Whitenoise](http://whitenoise.evans.io/en/stable/index.html)
- Styling with [Bootstrap v4](https://github.com/twbs/bootstrap)
- Debugging with [django-debug-toolbar](https://github.com/jazzband/django-debug-toolbar)
- DRY forms with [django-crispy-forms](https://github.com/django-crispy-forms/django-crispy-forms)

![Homepage](homepage.png)
----

## Table of Contents
* **[Installation](#installation)**
  * [Pip](#pip)
  * [Pipenv](#pipenv)
  * [Docker](#docker)
* [Next Steps](#next-steps)
* [Contributing](#contributing)
* [Support](#support)
* [License](#license)

----

## 📖 Installation
DjangoX can be installed via Pip, Pipenv, or Docker. To start, clone the repo to your local computer and change into the proper directory.

```
$ git clone https://github.com/wsvincent/djangox.git
$ cd djangox
```

### Pip

```
$ python -m venv .venv

# Windows
$ Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
$ .venv\Scripts\Activate.ps1

# macOS
$ source djangox/bin/activate

(.venv) $ pip install -r requirements.txt
(.venv) $ python manage.py migrate
(.venv) $ python manage.py createsuperuser
(.venv) $ python manage.py runserver
# Load the site at http://127.0.0.1:8000
```

### Pipenv

```
$ pipenv install
$ pipenv shell
(.venv) $ python manage.py migrate
(.venv) $ python manage.py createsuperuser
(.venv) $ python manage.py runserver
# Load the site at http://127.0.0.1:8000
```

### Docker

To use Docker with PostgreSQL as the database update the `DATABASES` section of `django_project/settings.py` to reflect the following:

```python
# django_project/settings.py
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "db",  # set in docker-compose.yml
        "PORT": 5432,  # default postgres port
    }
}
```

The `INTERNAL_IPS` configuration in `django_project/settings.py` must be also be updated:

```python
# config/settings.py
# django-debug-toolbar
import socket
hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS = [ip[:-1] + "1" for ip in ips]
```

And then proceed to build the Docker image, run the container, and execute the standard commands within Docker.

```
$ docker-compose up -d --build
$ docker-compose exec web python manage.py migrate
$ docker-compose exec web python manage.py createsuperuser
# Load the site at http://127.0.0.1:8000
```

## Next Steps

- Add environment variables. There are multiple packages but I personally prefer [environs](https://pypi.org/project/environs/).
- Add [gunicorn](https://pypi.org/project/gunicorn/) as the production web server.
- Update the [EMAIL_BACKEND](https://docs.djangoproject.com/en/4.0/topics/email/#module-django.core.mail) and connect with a mail provider.
- Make the [admin more secure](https://opensource.com/article/18/1/10-tips-making-django-admin-more-secure).
- `django-allauth` supports [social authentication](https://django-allauth.readthedocs.io/en/latest/providers.html) if you need that.

I cover all of these steps in my three books: [Django for Beginners](https://djangoforbeginners.com), [Django for APIs](https://djangoforapis.com), and [Django for Professionals](https://djangoforprofessionals.com).

----

## 🤝 Contributing

Contributions, issues and feature requests are welcome! See [CONTRIBUTING.md](https://github.com/wsvincent/djangox/blob/master/CONTRIBUTING.md).

## ⭐️ Support

Give a ⭐️  if this project helped you!

## License

[The MIT License](LICENSE)
