from django.db import models
from django.conf import settings

DEFAULT_CATEGORY_ID = 1
DEFAULT_USER_ID = 1

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Account(models.Model):
    name = models.CharField(max_length=50)
    site = models.CharField(max_length=50)
    html = models.CharField(max_length=150)
    username = models.CharField(max_length=50)
    password = models.BinaryField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=DEFAULT_USER_ID)
    category = models.ForeignKey(Category, 
        on_delete=models.SET_NULL,
        null=True)

    # def __str__(self):
    #     return self.name

