from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from .views import login_view, student_done
urlpatterns = [

    url(r'login$', login_view, name='login-student'),
    url(r'done$', student_done, name='student_done')


]