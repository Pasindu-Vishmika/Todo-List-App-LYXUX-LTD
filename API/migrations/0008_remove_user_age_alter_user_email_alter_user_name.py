# Generated by Django 5.0.4 on 2024-04-24 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0007_task_description_user_task_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='age',
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]