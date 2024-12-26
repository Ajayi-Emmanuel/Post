from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=200)
    content = models.TextField(max_length=1000, null=True)
    read_count = models.IntegerField(default=0, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title