# Generated by Django 3.0.2 on 2020-02-18 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0003_auto_20200218_1910'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='image',
            new_name='img',
        ),
    ]