"""leaderboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from board.views import home
from board.views import login
from board.views import register
from board.views import registerUser
from board.views import logOut
from board.views import rankBoard
from board.views import profile


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/',home),
    url(r'^login/',login),
    url(r'^register/',register),
    url(r'^registerUser/',registerUser),
    url(r'^logOut/',logOut),
    url(r'^profile/',profile),
    url(r'^rankBoard/',rankBoard)
]