# Generated by Django 3.1.2 on 2021-03-26 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(default='media/images/error-pic.png', help_text='Choose a picture', upload_to='media/images/'),
        ),
    ]
