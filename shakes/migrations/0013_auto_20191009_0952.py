# Generated by Django 2.2.5 on 2019-10-09 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shakes', '0012_attendance_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='userType',
            field=models.CharField(default='0', max_length=4),
        ),
    ]
