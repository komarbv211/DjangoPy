from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)  
    content = models.TextField()  
    slug = models.SlugField(null=True, unique=True, blank=True)                
    created_at = models.DateTimeField(auto_now_add=True) 
    image = models.ImageField(upload_to='posts_images/', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    def save(self, *args, **kwargs):
        if not self.slug: 
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title

