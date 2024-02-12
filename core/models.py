from django.db import models
from django.contrib.auth.models import AbstractUser

from django_ckeditor_5.fields import CKEditor5Field


class User(AbstractUser):

    username = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.get_full_name()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', "last_name", "username"]


class Document(models.Model):
    doc = models.FileField()
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name="authored")
    collaborators = models.ForeignKey(User, on_delete = models.SET_NULL, null= True, blank=True ,related_name = "colaborate_on")
    body = CKEditor5Field('Text', config_name='extends', blank = True)
    created = models.DateTimeField( auto_now_add=True)
    updated = models.DateTimeField(auto_now = True)

    def __str__(self) -> str:
        return f"{self.author}'s file"
    

