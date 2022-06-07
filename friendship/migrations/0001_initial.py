# Generated by Django 3.1.7 on 2021-03-26 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_profile', '0007_auto_20210326_1813'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friendship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='sendFriendRequest', max_length=50)),
                ('profile_one', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='profile_one', to='user_profile.userprofile')),
                ('profile_two', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='profile_two', to='user_profile.userprofile')),
            ],
        ),
    ]
