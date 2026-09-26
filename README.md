# resume-project

A personal resume / portfolio website built with Django 6 and Django REST Framework.
It serves a server-rendered Persian (fa-IR) single-page resume with skills, tools, a
learning timeline, projects, articles and a contact form, plus a JSON API for the same
data.

## Features

- **Home page** (`/`) — renders the superuser's profile, skills, tools, learning
  timeline, projects, articles and social links, and accepts contact-form submissions.
- **Blog** (`/blog/<slug>/`) — article detail pages, with rich text authored through
  CKEditor 5.
- **Admin** (`/admin/`) — content management for every model.
- **REST API** (`/api/`) — JWT-authenticated endpoints with OpenAPI schema and Swagger UI.
- **Custom user model** (`user_module.User`) — extends `AbstractUser` with `phone`,
  `about_user` and `more_about_me`.

## Project layout

| Path | Description |
| --- | --- |
| `msaeedahi/` | Django project settings, URL config, WSGI/ASGI entrypoints |
| `home/` | Core models (`Skill`, `Tools`, `Projects`, `TimeLineRoad`, `Article`, `ContactUsModel`, `SocialLinks`), home page view and contact form |
| `blog/` | Article detail view and template |
| `user_module/` | Custom `User` model |
| `api/` | DRF layer: `api/users/`, `api/blogs/`, `api/projects/` |
| `templates/`, `static/` | Shared templates and CSS/JS/images |

## Requirements

- Python 3.12+
- PostgreSQL
- The packages listed in `requirements.txt` (Django 6.0, DRF 3.18, SimpleJWT,
  drf-spectacular, django-filter, django-ckeditor-5, Pillow, psycopg2, python-decouple)

## Getting started

```bash
git clone https://github.com/saeedahi/resume-project.git
cd resume-project

python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Settings are read with `python-decouple`, so create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key
DEBUG=True

DB_NAME=resume
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=127.0.0.1
DB_PORT=5432
```

Then apply migrations, create the superuser whose profile the home page renders, and
start the development server:

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

The site is available at http://127.0.0.1:8000/ and the admin at
http://127.0.0.1:8000/admin/.

> The home page reads the first superuser account, so the profile fields (`phone`,
> `about_user`, ...) of that account should be filled in from the admin before the page
> shows meaningful content.

## API

Interactive documentation is served by drf-spectacular:

- OpenAPI schema: `/api/schema/`
- Swagger UI: `/api/schema/swagger/`

| Method | Endpoint | Description |
| --- | --- | --- |
| `POST` | `/api/token/` | Obtain a JWT access/refresh pair |
| `POST` | `/api/token/refresh/` | Refresh an access token |
| `POST` | `/api/users/register/` | Register a new user |
| `POST` | `/api/users/login/` | Log in and receive tokens |
| `GET`/`PUT`/`PATCH` | `/api/users/` | Read or update the authenticated user's profile |
| `GET`/`POST` | `/api/blogs/` | List or create articles |
| `GET`/`PUT`/`PATCH`/`DELETE` | `/api/blogs/<slug>/` | Retrieve or modify a single article |
| `GET` | `/api/projects/` | List projects |

Authentication uses `rest_framework_simplejwt`; send the access token as
`Authorization: Bearer <token>`. Responses are paginated (6 items per page) and support
filtering, search and ordering through `django-filter` and DRF's filter backends.

## Media and static files

Uploaded images are written to `uploads/` and served from `/medias/` during development.
Project static assets live in `static/`.

## Tests

```bash
python manage.py test
```
