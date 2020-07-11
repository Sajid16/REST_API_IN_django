from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 50, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']


class Articles(models.Model):
    name = models.CharField(max_length = 50, null=False)
    description = models.TextField(max_length = 50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']
