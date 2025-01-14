# Generated by Django 3.2.19 on 2023-06-23 17:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('fathername', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('profile_image', models.ImageField(upload_to='profiles/')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('user_type', models.CharField(choices=[('P', 'Principal'), ('T', 'Teacher'), ('S', 'Student')], max_length=1)),
                ('qr_code', models.ImageField(blank=True, upload_to='QRCodes/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
