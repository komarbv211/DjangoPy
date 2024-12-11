from django.db import models
from django.contrib.auth.hashers import make_password

class User(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=150)

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if not self.pk:  
            self.password = make_password(self.password)
        super(User, self).save(*args, **kwargs)
