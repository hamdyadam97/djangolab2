from django.db import models

The_Choices ={
    ('f','female'),
    ('m','male')
}


class Trainee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False)
    national_num = models.IntegerField(default=000000000)
    sex = models.CharField(choices=The_Choices, default=1, max_length=15)
    address = models.CharField(null=True,max_length=120)

    def __str__(self):
        return self.name
