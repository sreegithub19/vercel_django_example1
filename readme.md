- Steps to run:
  (Reference : https://jay-hale.medium.com/django-on-vercel-in-30-minutes-e69eed15b616)

  - - cd into the application directory
  - - django-admin startproject vercel_app .
  - - python manage.py startapp example
  - - Update your project settings to include example in the list of INSTALLED_APPS
  - - Fill "vercel_app/urls.py", "example/views.py" according to the above URL
  - - In "vercel_app/settings.py", add to ALLOWED_HOSTS:
  - - ALLOWED_HOSTS = ['localhost', '127.0.0.1','.vercel.app','frontend']
  - - python manage.py runserver

- Push to github:

  - git add . && git commit -m "Changes" && git push origin main

- Deploying to Vercel:

  - vercel login
  - Create and fill "requirements.txt" accordingly (pip show <package_name> -> for info on the package)
  - Create "vercel.json" in root folder, and fill it as shown in the file.
  - Add this line in "vercel_app/wsgi.py" : app = application
  - vercel # (for preview)
  - vercel --prod # (for production)

- Hiding secret key:

  - Create .env file in the directory as settings.py , and add it to .gitignore
  - Put the secret key in the .env file (from "settings.py")

- All in one:
- - git add . && git commit -m "Changes" && git push origin main && vercel && vercel --prod


- Versions used:
  - Python: 3.8.0
  - Django: 4.1.1
