
from django.urls import path 
from .views import *
urlpatterns = [
    path('', TodoGetAndCreateView.as_view(), name='todo'),
    path('update/<str:pk>/', TodoUpdateAndDeleteView.as_view(), name='update')
]