# Generated by Django 2.0 on 2019-06-01 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('origin', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='origin',
            name='image',
        ),
    ]