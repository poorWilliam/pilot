from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class userKhodam(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    mobile = models.CharField(max_length=11)
    email = models.EmailField(max_length=254)
    createdtime = models.DateField(auto_now=True)
    def __str__(self) -> str:
        return self.name.__str__()
    
class lesson(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.name.__str__()
    
class proffesor(models.Model):
    name = models.CharField(max_length=20)
    degrees =[
        {"sikl1", "sikl"},
        {"diplom1", "diplom"},
        {"kardani1", "kardani"},
        {"karshenasi1", "karshenasi"},
        {"karshenasi arshad1", "karshenasi arshad"},
        {"pro1", "pro"},
    ]
    degree = models.CharField(max_length=20, choices=degrees)
    lesson = models.CharField(max_length=20)
    def __str__(self) -> str:
        return f'{self.name.__str__()} / {self.degree.__str__()}'
class student(models.Model):
    name = models.CharField(max_length=20)
    lesson = models.CharField(max_length=20)
    proffesor = models.ForeignKey(proffesor, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f'name: {self.name.__str__()} / lesson: {self.lesson.__str__()} / proffesor: {self.proffesor.__str__()}'