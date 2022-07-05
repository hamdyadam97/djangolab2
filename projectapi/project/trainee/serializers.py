from rest_framework import serializers
from .models import *


class TraineeApi(serializers.ModelSerializer):
    class Meta:
        model = Trainee
        fields = '__all__'
