# Generated by Django 4.2.5 on 2023-10-03 19:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0005_student_remove_myuser_info_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="certificates",
            name="certificate",
            field=models.FileField(upload_to="auth/media/certificates"),
        ),
        migrations.AlterField(
            model_name="internships",
            name="internship",
            field=models.FileField(upload_to="auth/media/internships"),
        ),
        migrations.AlterField(
            model_name="reports",
            name="repot",
            field=models.FileField(upload_to="auth/media/repots"),
        ),
        migrations.AlterField(
            model_name="student",
            name="photo",
            field=models.FileField(upload_to="auth/media/profiles"),
        ),
    ]
