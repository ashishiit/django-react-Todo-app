# Generated by Django 2.2.4 on 2019-08-07 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0007_auto_20190807_1323'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='text',
            new_name='description',
        ),
    ]
