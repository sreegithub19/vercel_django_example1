"""vercel_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# vercel-django-example/example/urls.py
# https://github.com/jayhale/vercel-django-example/blob/main/example/urls.py#L7

from django.urls import path
from example.views import *

urlpatterns = [
    path('', index),
    path('chess', chess),
    path('calculator', calculator),
    path('maze', maze),
    path('sass_', sass_),
    path('codepen', codepen),
    path('tilt_maze', tilt_maze),
    path('dino', dino),
    path('solitaire', solitaire),
    path('sudoku', sudoku),
    path('puzzles', puzzles),
    path('tic_tac_toe', tic_tac_toe),
    path('clock', clock),
    path('hangman', hangman),
    path('virtual_keyboard', virtual_keyboard),
    
]