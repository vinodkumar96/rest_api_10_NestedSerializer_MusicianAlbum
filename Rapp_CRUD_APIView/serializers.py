from rest_framework import serializers,fields
from .models import Musician,Album

class MusicianSerializer (serializers.ModelSerializer):
    class Meta:
        model = Musician
        fields=('id','first_name','last_name','instrument','album_musician')

class AlbumSerializer (serializers.ModelSerializer):
    class Meta:
        model = Album
        fields=('id','artist','name','release_date','num_stars')
