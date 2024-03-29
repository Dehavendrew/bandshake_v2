# Generated by Django 2.2.5 on 2019-10-09 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_auto_20191008_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='image',
            field=models.ImageField(default='profile_pics\\default.jpg', upload_to='company_pics'),
        ),
        migrations.AlterField(
            model_name='flyer',
            name='file',
            field=models.FileField(null=True, upload_to='flyers'),
        ),
    ]
