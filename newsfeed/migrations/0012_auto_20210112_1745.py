# Generated by Django 3.0.4 on 2021-01-12 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsfeed', '0011_auto_20210112_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logaction',
            name='log_comment',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]
