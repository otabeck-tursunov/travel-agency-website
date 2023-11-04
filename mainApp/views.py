from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import *
from .models import *
from .serializers import *


# Service views
class ServiceListAPIView(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer




class ServiceRetrieveAPIView(RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


# Place views
class PlaceListAPIView(ListAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class PlaceRetrieveAPIView(RetrieveAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


# Action views
class ActionListAPIView(ListAPIView):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer


class ActionRetrieveAPIView(RetrieveAPIView):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer


# Employee views
class EmployeeListAPIView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeRetrieveAPIView(RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


# Contact views
class ContactCreateAPIView(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


# Comment views
class CommentListAPIView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentRetrieveAPIView(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer



