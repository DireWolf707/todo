# Generated by Django 3.2.3 on 2021-05-28 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='memo',
            new_name='description',
        ),
    ]