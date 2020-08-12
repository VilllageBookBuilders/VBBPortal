# Generated by Django 3.0.8 on 2020-08-12 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20200812_0004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mentorprofile',
            name='involvement',
        ),
        migrations.AddField(
            model_name='mentorprofile',
            name='desired_involvement',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='desired involvement'),
        ),
    ]
