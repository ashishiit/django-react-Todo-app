# Generated by Django 2.2.4 on 2019-08-07 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_auto_20190807_1302'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='name',
            new_name='title',
        ),
    ]
