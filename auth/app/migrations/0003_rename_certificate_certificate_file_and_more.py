# Generated by Django 4.2.5 on 2023-10-16 14:26

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0002_rename_durations_courseinternship_domain_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="certificate",
            old_name="certificate",
            new_name="file",
        ),
        migrations.RenameField(
            model_name="internship",
            old_name="internship",
            new_name="file",
        ),
        migrations.RenameField(
            model_name="report",
            old_name="report",
            new_name="file",
        ),
    ]
