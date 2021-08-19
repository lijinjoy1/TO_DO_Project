from django.db import models

# Create your models here.

class Tasks(models.Model):
    title=models.CharField(max_length=50)
    complete=models.BooleanField(default=False)
    created=models.DateField(auto_now_add=True)

def __str__(self):
    return self.title