# Generated by Django 3.2.8 on 2021-10-17 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarefa',
            name='texto',
            field=models.TextField(default=''),
        ),
    ]
