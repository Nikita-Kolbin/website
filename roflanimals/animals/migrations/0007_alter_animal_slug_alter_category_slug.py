# Generated by Django 4.1.7 on 2023-04-08 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0006_alter_animal_options_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='slug',
            field=models.SlugField(max_length=255, unique=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=255, unique=True, verbose_name='URL'),
        ),
    ]