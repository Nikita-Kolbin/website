# Generated by Django 4.1.7 on 2023-04-01 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0002_animal_viki_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animal',
            old_name='viki_link',
            new_name='wiki_link',
        ),
    ]
