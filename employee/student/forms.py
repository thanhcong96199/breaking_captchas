from django import forms
from django.contrib.auth import authenticate, password_validation
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.db import transaction
from django.template import loader

from .models import Student
import random

import datetime
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt
import numpy as np

import os
import time

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os
import json
import glob
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tensorflow.keras.models import load_model
import tensorflow as tf
import matplotlib.pyplot as plt
from PIL import Image
import glob, os, numpy as np
from captcha.image import ImageCaptcha




class StudentAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput(attrs={'placeholder': '********', 'class': "password"}))
    email = forms.EmailField(label='Email', max_length=60,
                             widget=forms.TextInput(attrs={'placeholder': 'sample@sample.co.jp', 'class': "email"}))
    input_text = forms.CharField(label='Input Text', widget=forms.TextInput(attrs={'class': 'input_text'}))
    image = 'assets/student/image/012u.png'

    class Meta:
        model = Student
        fields = ['email', 'password','input_text']

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            Student.objects.get(email=email)
        except:
            raise forms.ValidationError("Invalid email or password")
        return email

    def clean_password(self):
        password = self.cleaned_data['password']
        if self.is_valid():
            email = self.cleaned_data['email']
            try:
                authenticate(email_student=email, password_student=password)
            except:
                raise forms.ValidationError("Invalid email or password")
        return password

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email_student=email, password_student=password):
                raise forms.ValidationError('Invalid login')