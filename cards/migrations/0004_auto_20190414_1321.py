# Generated by Django 2.2 on 2019-04-14 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0003_studyset_is_public'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cards',
            new_name='Card',
        ),
    ]
