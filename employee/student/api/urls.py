from django.conf.urls import url

from student.api.views import get_new_image

urlpatterns = [
    url(r'^get-image$', get_new_image, name='get-image'),

]
