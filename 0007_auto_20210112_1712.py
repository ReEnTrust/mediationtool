# Generated by Django 3.0.4 on 2021-01-12 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsfeed', '0006_auto_20210112_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logaction',
            name='log_comment',
            field=models.CharField(default='no comment', max_length=2000),
        ),
    ]
