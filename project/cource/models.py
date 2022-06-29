from django.db import models

# Create your models here.
from  trainee.models import Trainee


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,null=False)
    slug = models.ForeignKey(Trainee,on_delete=models.CASCADE)
    grade = models.CharField(max_length=10, null=False)

    def __str__(self):
        return self.name