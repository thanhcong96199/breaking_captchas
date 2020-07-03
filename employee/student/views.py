from django.contrib.auth import login, authenticate, logout
from rest_framework import status
from django.shortcuts import redirect, render, Http404
from rest_framework.response import Response
from student.constants import label_file, path, path_folder
import os
from rest_framework.decorators import api_view

@api_view(['GET', 'PUT', 'DELETE', 'POST'])
def login_view(request):
    print(label_file)
    if request.POST:
        email_student = request.POST.get('email')
        password_student = request.POST.get('password')
        text_captcha = request.POST.get('textcaptcha')
        image = request.POST.get('image')
        image_path = os.path.join(path)

        error_response = {}

        if (email_student == 'tuyet@gmail.com' and password_student == '123456a@' and (text_captcha, image_path) in label_file):
            return Response({'success': 'success'})
        elif (email_student != 'tuyet@gmail.com' or password_student != '123456a@'):
            error_response['error_email_password'] = 'Email or password is wrong'
        if not ((text_captcha, image_path) in label_file):
            error_response['error_captcha'] = 'Text of Captcha is wrong'

        return Response(error_response)


    return render(request, 'user/login.html')


def student_done(request):
    return render(request, 'user/mess.html')