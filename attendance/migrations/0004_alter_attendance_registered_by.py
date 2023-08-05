# Generated by Django 3.2.19 on 2023-06-23 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('attendance', '0003_alter_attendance_registered_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='registered_by',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='registration', to='accounts.userprofile'),
        ),
    ]
