# Generated by Django 2.2.1 on 2019-05-29 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20190527_1911'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='image',
        ),
    ]
