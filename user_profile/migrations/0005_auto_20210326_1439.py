# Generated by Django 3.1.2 on 2021-03-26 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0004_auto_20210326_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar_profile',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
