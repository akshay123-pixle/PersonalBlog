# Generated by Django 5.0.3 on 2024-05-27 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_like'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='like',
            new_name='likes',
        ),
    ]
