# Generated by Django 2.2.6 on 2019-10-31 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoCMSapp', '0013_remove_post_comment_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100)),
                ('Email', models.EmailField(blank=True, max_length=100, null=True, unique=True)),
                ('profile_picture', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Contect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=100)),
                ('Messages', models.TextField(max_length=500)),
            ],
        ),
    ]