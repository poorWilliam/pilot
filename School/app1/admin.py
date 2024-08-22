from django.contrib import admin
from .models import lesson,proffesor,student,userKhodam
# Register your models here.
admin.site.register(lesson)
admin.site.register(proffesor)
admin.site.register(student)
@admin.register(userKhodam)
class userKhodamadmin(admin.ModelAdmin):
    pass
