from django.db import models

# Create your models here.


class The_User(models.Model):
    username = models.CharField(max_length=50, null=False)
    email = models.EmailField(null=False)
    password = models.CharField(max_length=50, null=False)
    confirm_password = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.username

