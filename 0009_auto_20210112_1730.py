# Generated by Django 3.0.4 on 2021-01-12 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsfeed', '0008_remove_logaction_log_comment'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LogAction',
            new_name='LogActionVote',
        ),
    ]