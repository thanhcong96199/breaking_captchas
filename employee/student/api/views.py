from django.db.models import Q, Prefetch, Count
from rest_framework import generics, status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
import os, random
from student.constants import files

path_folder = os.path.dirname(os.path.dirname(os.path.abspath('image')))
path = os.path.join(path_folder, 'employee/static/assets/student/image/imagetest')
files = os.listdir(path)


@api_view(['GET', 'PUT', 'DELETE'])
def get_new_image(req):
    index = random.randrange(0, len(files))

    url = '/static/assets/student/image/imagetest/'+files[index]
    return Response({'url':url})