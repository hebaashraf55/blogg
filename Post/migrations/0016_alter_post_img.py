# Generated by Django 4.0.6 on 2022-08-23 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0015_alter_post_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(default='post_img/default.png', upload_to='post_img/'),
        ),
    ]
