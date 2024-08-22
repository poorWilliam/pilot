from django.contrib import admin

# Register your models here.
from .models import artist
@admin.register(artist)
class productadmin(admin.ModelAdmin):
    pass
from .models import song
@admin.register(song)
class productadmin(admin.ModelAdmin):
    pass
