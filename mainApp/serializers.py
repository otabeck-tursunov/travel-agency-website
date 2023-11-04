from rest_framework.serializers import ModelSerializer
from .models import *

class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class PlaceSerializer(ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'


class ActionSerializer(ModelSerializer):
    class Meta:
        model = Action
        fields = '__all__'


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

