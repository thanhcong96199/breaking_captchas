from django.db import transaction
from rest_framework import serializers
from student.models import LoadAndGenImage

class LoadAndGenImageSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = LoadAndGenImage
        fields = ['url']