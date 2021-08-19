# Generated by Django 3.1.2 on 2021-08-17 16:15

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210809_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='passcode',
            field=models.CharField(default=main.models.generate_random_passcode, max_length=30),
        ),
    ]
