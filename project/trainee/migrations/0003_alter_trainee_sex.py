# Generated by Django 4.0.5 on 2022-06-29 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainee', '0002_alter_trainee_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainee',
            name='sex',
            field=models.CharField(choices=[('m', 'male'), ('f', 'female')], default=1, max_length=15),
        ),
    ]
