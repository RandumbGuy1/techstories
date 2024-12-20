# Generated by Django 5.1.2 on 2024-11-07 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_profile_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='posts',
        ),
        migrations.AddField(
            model_name='profile',
            name='followers',
            field=models.ManyToManyField(blank=True, to='catalog.profile'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='post_images'),
        ),
    ]
