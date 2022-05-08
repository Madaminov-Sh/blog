from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.template.defaultfilters import slugify


class User(AbstractUser):
    pass


class Post(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to="static/images/", default="models/default.jpg")
    slug = models.SlugField(max_length=30, null=False, unique=True)
    author = models.ForeignKey('Autor', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("core:detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):  
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

class Autor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username