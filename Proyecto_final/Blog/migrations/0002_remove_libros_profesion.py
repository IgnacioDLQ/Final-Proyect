# Generated by Django 4.1.3 on 2022-11-19 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libros',
            name='profesion',
        ),
    ]
