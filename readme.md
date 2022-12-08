Steps to run:
(Reference: https://jay-hale.medium.com/django-on-vercel-in-30-minutes-e69eed15b616)

- cd into the application directory
- django-admin startproject vercel_app .
- python manage.py startapp example
- Update your project settings to include example in the list of INSTALLED_APPS
- Fill "vercel_app/urls.py", "example/views.py" according to the above URL
- In "vercel_app/settings.py", add to ALLOWED_HOSTS:
  - ALLOWED_HOSTS = ['localhost', '127.0.0.1','.vercel.app','frontend']
- python manage.py runserver

- Push to github:
  - git add . && git commit -m "Changes" && git push origin main
- Versions used:
  - Python: 3.8.0
