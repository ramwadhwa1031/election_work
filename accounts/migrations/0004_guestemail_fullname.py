# Generated by Django 2.1.2 on 2019-03-15 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='guestemail',
            name='fullname',
            field=models.CharField(default='', max_length=200),
        ),
    ]
