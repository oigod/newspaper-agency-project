# Newspaper Agency Project

Django project for managing newspaper and redactors in a newspaper agency.


## Check the project:

- [x] [Newspaper Agency](https://newspaper-agency-z8y6.onrender.com/)


## Requirements:

Python3 must be installed in your system.


```shell
git clone https://github.com/oigod/newspaper-agency-project.git
cd newspaper-agency-project
python3 -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
## Environmental variables:
```shell
DJANGO_SETTINGS_MODULE=config.settings;
DJANGO_DEBUG=True
DATABASE_URL=*provide link for your database here*
```

## Features:
* [x] Create, update and delete newspaper
* [x] Create, update and delete redactor
* [x] Create, update and delete article
* [x] Authentication and Registration
* [x] Admin panel


## Test User:
* [x] Username: user_test
* [x] Password: 1qazcde3

## Demo View:
![Screenshot](project%20demo.png)