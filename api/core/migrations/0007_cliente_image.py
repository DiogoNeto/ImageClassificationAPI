# Generated by Django 2.2.1 on 2019-05-29 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_remove_cliente_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='image',
            field=models.ImageField(blank=True, max_length=255, upload_to='pictures/%Y/%m/%d/'),
        ),
    ]
