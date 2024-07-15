from django.shortcuts import render
from rest_framework import generics
from .serializers import TodoSerializer
from .models import Todoapp

# Create your views here.

class TodoGetAndCreateView(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    queryset = Todoapp.objects.all()


class TodoUpdateAndDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    queryset = Todoapp.objects.all()
    lookup_field = 'pk'