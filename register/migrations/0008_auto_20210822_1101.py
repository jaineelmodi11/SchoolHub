# Generated by Django 3.1.2 on 2021-08-22 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0007_auto_20210822_1051'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='isCreater',
            new_name='isCreator',
        ),
    ]
