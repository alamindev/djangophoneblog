# Generated by Django 2.2.6 on 2019-10-31 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoCMSapp', '0014_about_contect'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Front_camera',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='post',
            name='display',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='post',
            name='os',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='post',
            name='processor',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='post',
            name='storage',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
