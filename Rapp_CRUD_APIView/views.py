from django.shortcuts import render
from .models import Musician,Album
from .permissions import permission
from .serializers import MusicianSerializer,AlbumSerializer
from rest_framework import generics
# Create your views here.
class M_View(generics.ListCreateAPIView):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer
class ML_View(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MusicianSerializer
    queryset = Musician.objects.all()

class A_View(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
class AL_View(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()
