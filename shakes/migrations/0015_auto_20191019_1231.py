# Generated by Django 2.2.5 on 2019-10-19 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shakes', '0014_attendance_fileshared'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='fileShared',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.flyer'),
        ),
    ]