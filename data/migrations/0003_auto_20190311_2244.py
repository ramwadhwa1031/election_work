# Generated by Django 2.1.2 on 2019-03-11 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20190310_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post',
            field=models.CharField(choices=[('Admin', 'Admin'), ('User', 'User'), ('XYZ', 'XYZ')], max_length=30),
        ),
    ]
