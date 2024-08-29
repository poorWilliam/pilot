from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, nationalcode, password=None):
        if not nationalcode:
            raise ValueError('Users must have an nationalcode')
        user = self.model(
            nationalcode = nationalcode
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, nationalcode, password):
        user = self.create_user(
            nationalcode=nationalcode,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    nationalcode = models.IntegerField(unique=True, max_length=10)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = 'nationalcode'
    def __str__(self):
        return self.nationalcode
    def has_perm(self, perm, obj=None):
        return True
    def has_module_perms(self, app_label):
        return True
    @property
    def is_staff(self):
        return self.is_admin