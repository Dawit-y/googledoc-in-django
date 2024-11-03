from django.db import models
from django.contrib.auth.models import AbstractUser

from django_quill.fields import QuillField


class User(AbstractUser):

    username = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.get_full_name()

    def save(self, *args, **kwargs):
        if self.pk is None:  # New user
            if not self.password.startswith('pbkdf2_'):  # Check if password is already hashed
                self.set_password(self.password)  # Hash the password
        super().save(*args, **kwargs)  # Call the superclass save method
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', "last_name", "username"]


class Document(models.Model):
    name = models.CharField(max_length = 150, blank=True, null = True)
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name="authored")
    collaborators = models.ManyToManyField(User, blank=True ,related_name = "colaborated_on")
    body =  models.TextField(null=True, blank=True)
    created = models.DateTimeField( auto_now_add=True)
    updated = models.DateTimeField(auto_now = True)

    def __str__(self) -> str:
        return f"{self.author}'s file {self.id}"

