from django.urls import path
from .views import *

urlpatterns = [
    path('services/', ServiceListAPIView.as_view()),
    path('service/<int:pk>/', ServiceRetrieveAPIView.as_view()),

    path('places/', PlaceListAPIView.as_view()),
    path('place/<int:pk>/', PlaceRetrieveAPIView.as_view()),

    path('actions/', ActionListAPIView.as_view()),
    path('action/<int:pk>/', ActionRetrieveAPIView.as_view()),

    path('employees/', EmployeeListAPIView.as_view()),
    path('employee/<int:pk>/', EmployeeRetrieveAPIView.as_view()),

    path('contacts/', ContactCreateAPIView.as_view()),

    path('comments/', CommentListAPIView.as_view()),
    path('comment/<int:pk>/', CommentRetrieveAPIView.as_view()),


]