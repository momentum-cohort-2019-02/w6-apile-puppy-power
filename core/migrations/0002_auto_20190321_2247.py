# Generated by Django 2.1.7 on 2019-03-22 03:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vote',
            old_name='post',
            new_name='postlink',
        ),
    ]