# Generated by Django 2.2.5 on 2019-09-16 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profile_pics\\default.jpg', upload_to='profile_pics'),
        ),
    ]