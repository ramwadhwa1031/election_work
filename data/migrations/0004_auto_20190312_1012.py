# Generated by Django 2.1.2 on 2019-03-12 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_auto_20190311_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post',
            field=models.CharField(choices=[('a', 'a'), ('b', 'b'), ('c', 'c')], max_length=30),
        ),
    ]
