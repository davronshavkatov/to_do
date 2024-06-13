from django.db import models

class Task(models.Model):
    task= models.CharField(max_length=200)
    is_complected = models.BooleanField(default=False)
    created = models.DateField(auto_now=True)
    update = models.DateField(auto_now=True)

    def __str__(self):
        return self.task

