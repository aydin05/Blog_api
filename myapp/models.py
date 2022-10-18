from django.contrib.auth.models import User
from django.db import models

from rest_framework.authtoken.models import Token


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.FileField(upload_to='post_images')
    category = models.ForeignKey('Category', related_name='posts', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


def __str__(self):
    return f'{self.title} {self.update_at} | {self.published}'


class Category(models.Model):
    name = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

#
# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)
