from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from .views import login_view
urlpatterns = [

    url(r'login$', login_view, name='login-student'),


]