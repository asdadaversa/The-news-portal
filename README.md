# The-news-portal Api
Api for News Portal Service written on DRF. Celery, Redis, Djoser, Google Auth.
Parsing news with Selenium, Beautifulsoup, requests


## Features
- JWT Token authenticated
- Admin panel /admin/
- Create user, edit and delete your own profile.
- Email confirmation registration, reset password and username with email.
- Login with your own google account.
- Creating and updating News
- Parsing news with Selenium, Beautifulsoup, requests 
- Search news by title, text, date, source

## API Endpoints
<details>
  <summary>Users</summary>

- **Create User**: `POST /api/users/`
- **Login**: `POST /api/users/token/`
- **Login**: `POST /api/users/refresh/`
- **Login**: `POST 
- **Retrieve User Profile**: `GET /api/users/me/`
- **Put User Profile**: `PUT /api/users/me/`
- **Delete User Profile**: `DELETE /api/users/me/`
- 
- **Activation**: `POST api/users/activation/{uid}/{token}/`
- **Resend Activation**: `POST api/users/resend_activation/`
- **Set Password**: `POST api/users/set_password/`
- **Reset Password**: `POST api/users/reset_password/`
- **Reset Password Confirm**: `POST api/users/reset_password_confirm/{uid}/{token}/`
- **Set Username**: `POST api/users/set_username/`
- **Reset Username Confirm**: `POST api/users/reset_username_confirm/{uid}/{token}/`
- **Logout**: `POST api/users/logout/`

</details>


<details>
  <summary>Fresh News</summary>

- **List News**: `GET /api/books/`
- **Create News**: `POST /api/books/`
- **Retrieve News**: `GET /api/books/{neews_id}/`
- **Update News**: `PUT /api/books/{neews_id}/`
- **Delete News**: `DELETE /api/books/{neews_id}/`

</details>

### Installing using GitHub
Python3 must be already installed. Install PostgresSQL and create db.


```shell
git clone https://github.com/asdadaversa/The-news-portal.git
cd the-news-portal
python3 -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)
pip install -r requirements.txt
```

### Next run migrations and run server

```bash
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver

```

## Use the following command to load prepared data from fixture:

`python manage.py loaddata data.json`

- After loading data from fixture you can use following superuser (or create another one by yourself):
  - email: `admin@example.com`
  - Password: `Qwerty.1`

## Getting access:
  - Create user - /api/users/
  - Get access token - /api/users/token/

  - You can load ModHeader extension for your browser and add request header token. Example:
  - key: Authorize
  - value:Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE1ODA4NzYzLCJpYXQiOjE3MTU3OTA3NjMsImp0aSI6IjdmNThkOWRjODhmNjQwODdhZDdmNGZjNjRlZTBhMTdmIiwidXNlcl9pZCI6Mn0.o0Em-E0y47llU5hUJt57R3dLGvMDIEgvBi0TR8ElouE

## Getting access via google account:
  - login - /social-auth/login/google-oauth2/

### Celery setup
```
celery -A library_service worker --loglevel=INFO
CELERY_BROKER_URL=redis://localhost:6379/1
CELERY_RESULT_BACKEND=redis://localhost:6379/2
```

### Environment Variables Setup
1. Create a `.env` file in the root directory of your project.
2. Set up it as in '.env.sample'
```
SECRET_KEY=SECRET_KEY
POSTGRES_HOST=POSTGRES_HOST
POSTGRES_DB=POSTGRES_DB
POSTGRES_USER=POSTGRES_USER
POSTGRES_PASSWORD=POSTGRES_PASSWORD
DB_PORT=DB_PORT
CELERY_BROKER_URL='redis://localhost/1'
CELERY_RESULT_BACKEND='redis://localhost/2'
```

## Run with docker
Docker should be installed
```
set up your .env for docker, for e.g.
POSTGRES_HOST=db
POSTGRES_DB=app
POSTGRES_USER=postgres
POSTGRES_PASSWORD=secretpassword
CELERY_BROKER_URL=redis://localhost:6379/1
CELERY_RESULT_BACKEND=redis://localhost:6379/2

next run:
- docker-compose build
- docker-compose up

create superuser:
docker-compose run app python manage.py createsuperuser

```

## Contributing
Feel free to contribute to these enhancements, and let's make our Library Service API even better!
