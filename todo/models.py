from django.db import models

# Create your models here.


class Todo(models.Model):
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField()

    def __str__(self):
        return self.description
