from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # User é do próprio Django
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)  # cria automaticamente o horário do post
    updated = models.DateTimeField(auto_now=True)  # atualiza automaticamente quando post for modificado

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blogapp:detail", kwargs={"slug": self.slug})
