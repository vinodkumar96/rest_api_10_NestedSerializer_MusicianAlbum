from django.contrib import admin
from .models import Musician,Album
# Register your models here.

class MusicianAdmin (admin.ModelAdmin):
    list_display = ('first_name','last_name','instrument')
admin.site.register(Musician,MusicianAdmin)


class AlbumAdmin (admin.ModelAdmin):
    list_display = ('artist','name','release_date','num_stars')
admin.site.register(Album,AlbumAdmin)
