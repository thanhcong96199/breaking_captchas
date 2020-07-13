from django.db.models import Q, Prefetch, Count
from rest_framework import generics, status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from tensorflow.keras.models import load_model
import tensorflow as tf
import os, random, numpy as np
from student.constants import files, show_label
from PIL import Image
from tensorflow.python.keras.backend import set_session
from tensorflow.python.keras.models import load_model
import keras
from keras import backend as K



path_folder = os.path.dirname(os.path.dirname(os.path.abspath('image')))
path = os.path.join(path_folder, 'employee/static/assets/student/image/imagetest')
files = os.listdir(path)
global graph
graph = tf.get_default_graph()






@api_view(['GET', 'PUT', 'DELETE'])
def get_new_image(req):


    # with graph.as_default():
    #     result = model.predict(np.expand_dims(im, axis=0))
    index = random.randrange(0, len(files))
    url = '/static/assets/student/image/imagetest/' + files[index]
    path_image = path + '/' + files[index]
    model = load_model('model-050-0.976878-0.974703.h5')
    image = Image.open(path_image)
    image = image.resize((120, 100))
    im = np.array(image) / 255.0
    result = model.predict(np.expand_dims(im, axis=0))
    value = show_label(result[0])

    return Response({'url':url, 'value': value})