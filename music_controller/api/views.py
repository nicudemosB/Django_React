from django.shortcuts import render
from rest_framework import generics
from .serializer import RoomSerializer
from .models import Room
# Create your views here.
# //endpoints go here//

class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

