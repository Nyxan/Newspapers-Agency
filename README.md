# Newspapers-Agency

Django project for posting news, managing redactors and news

[Newspapers Agency deployed to render](https://newspapers-agency-fbbi.onrender.com/)

## Installing / Getting started

Python3 must be already installed

```shell
git clone https://github.com/Nyxan/Newspapers-Agency
cd Newspapers-Agency
python3 -m venv venv
source venv/scripts/activate
pip install -r requirements.txt
python manage.py runserver
```

## Configuration

If you need add email verification possibility in newspaper_agency/settings.py
change ACCOUNT_EMAIL_VERIFICATION='none' on ACCOUNT_EMAIL_VERIFICATION='mandatory'

## Features

* Authentification functionality with email verification(disabled by default)
* Managing newspapers, redactors & topics
* Search system for searching by topic
* If you get really randy, you can even do this
* Powerful admin panel for advanced managing

Project in develop
