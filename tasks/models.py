from django.db import models

#Simple Task object
class Task(models.Model):
    name = models.CharField(max_length=60)
    deadline = models.DateTimeField()
    details = models.TextField()

    def __str__(self):
        return self.name
