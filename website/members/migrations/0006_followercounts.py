# Generated by Django 4.2.1 on 2023-09-18 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_likepost'),
    ]

    operations = [
        migrations.CreateModel(
            name='FollowerCounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.CharField(max_length=100)),
                ('user', models.CharField(max_length=100)),
            ],
        ),
    ]