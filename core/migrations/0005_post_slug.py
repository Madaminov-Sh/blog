# Generated by Django 4.0.4 on 2022-04-28 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=5, max_length=30),
            preserve_default=False,
        ),
    ]
