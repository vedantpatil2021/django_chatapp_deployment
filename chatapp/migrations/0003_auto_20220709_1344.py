# Generated by Django 3.0.14 on 2022-07-09 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0002_auto_20220708_2153'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='room',
            new_name='room_name',
        ),
    ]
