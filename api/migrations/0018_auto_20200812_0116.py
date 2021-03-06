# Generated by Django 3.0.8 on 2020-08-12 08:16

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0017_mentorprofile_initials'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='notes',
        ),
        migrations.RemoveField(
            model_name='computer',
            name='computer_num',
        ),
        migrations.RemoveField(
            model_name='library',
            name='calendar_name',
        ),
        migrations.AddField(
            model_name='appointment',
            name='mentor_notes',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='computer',
            name='computer_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='mentorprofile',
            name='advisor_notes',
            field=models.TextField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='event_id',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='hsm',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(167)], verbose_name='hours since monday at 12am (eastern time)'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Language'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='mentee_computer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='appointments', to='api.Computer'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='mentor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='appointments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='computer',
            name='computer_email',
            field=models.EmailField(max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='computer',
            name='language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='computers', to='api.Language'),
        ),
        migrations.AlterField(
            model_name='computer',
            name='library',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='computers', to='api.Library'),
        ),
        migrations.AlterField(
            model_name='computer',
            name='room_id',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='language',
            name='name',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='library',
            name='calendar_id',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='library',
            name='library_classroom',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='library',
            name='library_gmail_group',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='library',
            name='name',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='library',
            name='program_director_email',
            field=models.EmailField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='library',
            name='program_director_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='library',
            name='program_director_phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='library',
            name='time_zone',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='library',
            name='whatsapp_group',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='mentorprofile',
            name='affiliation',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='mentorprofile',
            name='desired_involvement',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='mentorprofile',
            name='first_name',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='mentorprofile',
            name='initials',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='mentorprofile',
            name='last_name',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='mentorprofile',
            name='occupation',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='mentorprofile',
            name='personal_email',
            field=models.EmailField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='mentorprofile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='mentorprofile',
            name='referral_source',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='mentorprofile',
            name='time_zone',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='mentorprofile',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mp', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='mentorprofile',
            name='vbb_email',
            field=models.EmailField(max_length=60, null=True),
        ),
    ]
