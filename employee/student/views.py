from django.contrib.auth import login, authenticate, logout
from rest_framework import status
from django.shortcuts import redirect, render, Http404
from rest_framework.response import Response
from student.constants import label_file, path, path_folder, value_label
import os
from rest_framework.decorators import api_view
from student.models import Student
from django.db.models import Q

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
        student = Student.objects.filter(Q(email=email_student) & Q(password=password_student))
        if (student and text_captcha in value_label):
            return Response({'success': 'success'})
        elif not student:
            error_response['error_email_password'] = 'Email or password is wrong'
        if not (text_captcha in value_label):
            error_response['error_captcha'] = 'Text of Captcha is wrong'

        return Response(error_response)


    return render(request, 'user/login.html')


def student_done(request):
    return render(request, 'user/mess.html')