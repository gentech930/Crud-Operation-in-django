from django.db import models
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=25, null=False)
    password = models.CharField(max_length=15, null=True)
    def __str__(self):
        return self.name
