
## 🚀 About Me
I'm a python developer from Belarus 🧚‍♂️

[![Linkedin Badge](https://img.shields.io/badge/-HannaKatsko-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/midhruvjaink/)](https://www.linkedin.com/in/hanna-katsko-a4319222b)
 
# 🧞 Horoscope Web Site

Horoscope web site is a resourse of information about zodiac signs. All articles is stored in a DataBase, so you can provide this project with your own description of each zodiac sign throught the Django admin panel.
This website pulls daily Horoscope out of https://horo.mail.ru/ using a [Beautiful Soul](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) python package.
The user can send any zodiac sign's Horoscope to a friend with email.
The Web site provides the Django authorization system to use his Daily Notes.
Daily Notes is a section where user can write some notes and use this section as a Diary. 

A few screenshots 👇👇👇

The home page. 
![Image alt](https://github.com/annkatsko/client-calendar-readme-img/raw/main/img11.png)

The page where you can learn your Zodiac Sign. 
![Image alt](https://github.com/annkatsko/client-calendar-readme-img/raw/main/img10.png)

The information page of Zodiac Sign. 
![Image alt](https://github.com/annkatsko/client-calendar-readme-img/raw/main/img9.png)
## 👨‍💻 Project stack
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)

[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://docs.djangoproject.com/en/4.1/)

![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

![HTML](https://img.shields.io/badge/HTML-239120?style=for-the-badge&logo=html5&logoColor=white)

![CSS](https://img.shields.io/badge/CSS-239120?&style=for-the-badge&logo=css3&logoColor=white)

![JS](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

![Bootstrap](	https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)


## 	🚀 Deployment
You need Python 3.10.8 and pip (the package installer for Python). 

To deploy this project run

```bash
  pip install -r requirements.txt
```
Than create your superuser and provide it with username and password. 

```bash
  python manage.py createsuperuser
```


## Settings.py

```python
SECRET_KEY = "generate your secret key"

# email configs
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'your email'
EMAIL_HOST_PASSWORD = "your email passwords"
DEFAULT_FROM_EMAIL="your default email"
DEFAULT_TO_EMAIL=env"your default email to send to"
```

Note:
it's worth storing all credentials in .env file.
Example:
```python
import environ
# Initialise environment variables
env = environ.Env()
environ.Env.read_env()
EMAIL_HOST_USER = env("EMAIL_USER")
```

Than run next commands in the console from the root directory:
```python
python manage.py makemigrations
```
```python
python manage.py migrate
```
```python
python manage.py runserver
```

Now you should all information you want about Zodiac Signs via django admin panel.

Go to http://127.0.0.1:8000/admin/ and login via your superuser creds. 
After that provide all Models and their fields with information. This information will be displayed on the web site. 


Congratulations 🎉  You have done it 🥇






## ✏️ Contributing
1. Fork it (https://github.com/annkatsko/myhoroscope.com/fork). 
2. Create your feature branch (git checkout -b feature/fooBar). 
3. Commit your changes (git commit -am ‘Add some fooBar’). 
4. Push to the branch (git push origin feature/fooBar). 
5. Create a new Pull Request. 


## 🦸‍♀️ Authors

- [@annkatsko](https://github.com/annkatsko)

