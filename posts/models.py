from operator import mod
from this import d
from django.db import models
from accounts.models import User
# Create your models here.
class Posts(models.Model):
    FACULTY_CHOICES=[("BEI",'BEI'),("BCT",'BCT'),("BCE","BCE")]
    SEM_CHOICES=[("I/I",'I/I'),("I/II",'I/II'),("III/I","III/I"),("IV/I","IV/I"),("IV/II","IV/II")]
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    file=models.FileField(default="default.jpg")
    caption=models.TextField(null=True,blank=True)
    faculty=models.CharField(choices=FACULTY_CHOICES,max_length=10)
    sem=models.CharField(choices=SEM_CHOICES,max_length=10)  
    sub=models.TextField(null=True,blank=True,max_length=20)
 

    def __str__(self):
        return str(self.caption)

class Review(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    post=models.ForeignKey(Posts,on_delete=models.CASCADE,null=True,blank=True)
    comment=models.TextField(max_length=250,null=True,blank=True)
    rate=models.IntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __Str__(self):
        return str(self.comment)
