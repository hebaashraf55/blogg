# Generated by Django 4.0.6 on 2022-08-03 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0002_alter_post_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(blank='null', null='', upload_to='post_image/'),
        ),
    ]
