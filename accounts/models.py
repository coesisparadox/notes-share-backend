from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .manager import UserManager


class User(AbstractBaseUser,PermissionsMixin):
    FACULTY_CHOICES=[("BEI",'BEI'),("BCT",'BCT'),("BCE","BCE")]
    SEM_CHOICES=[("I/I",'I/I'),("I/II",'I/II'),("III/I","III/I"),("IV/I","IV/I"),("IV/II","IV/II")]
    username=None
    email = models.EmailField(unique=True)
    faculty=models.CharField(choices=FACULTY_CHOICES,null=False,max_length=10)
    sem=models.CharField(choices=SEM_CHOICES,null=False,max_length=10)
    created = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return str(self.email)