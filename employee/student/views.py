from django.contrib.auth import login, authenticate, logout
from rest_framework import status
from django.shortcuts import redirect, render, Http404
from rest_framework.response import Response
from student.constants import label_file, path_folder
import os


def login_view(request):
    print(label_file)
    if request.POST:
        email_student = request.POST.get('email')
        password_student = request.POST.get('password')
        text_captcha = request.POST.get('textcaptcha')
        image = request.POST.get('image')
        image_path = os.path.join(path_folder, image)

        if (email_student == 'tuyet@gmail.com' and password_student == '123456a@' and (text_captcha, image_path) in label_file):
            return render(request, 'user/mess.html')
        else:
            return render(request, 'user/login.html')

    return render(request, 'user/login.html')