# Generated by Django 2.2.5 on 2019-09-28 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shakes', '0006_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='act',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='resume',
            name='address',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='resume',
            name='edu',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='resume',
            name='email',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='resume',
            name='exp',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='resume',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='resume',
            name='phone',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='resume',
            name='skills',
            field=models.CharField(default='', max_length=150),
        ),
    ]
