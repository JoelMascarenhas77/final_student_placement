# Generated by Django 4.2.5 on 2023-09-30 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0002_certificates_internships_reports_student_info_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="certificates",
            old_name="certificates",
            new_name="certificate",
        ),
        migrations.RenameField(
            model_name="internships",
            old_name="internships",
            new_name="internship",
        ),
        migrations.RenameField(
            model_name="reports",
            old_name="repots",
            new_name="repot",
        ),
        migrations.RemoveField(
            model_name="student_info",
            name="certificates",
        ),
        migrations.RemoveField(
            model_name="student_info",
            name="internships",
        ),
        migrations.RemoveField(
            model_name="student_info",
            name="reports",
        ),
        migrations.AddField(
            model_name="certificates",
            name="key",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="app.student_info",
            ),
        ),
        migrations.AddField(
            model_name="internships",
            name="key",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="app.student_info",
            ),
        ),
        migrations.AddField(
            model_name="reports",
            name="key",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="app.student_info",
            ),
        ),
    ]
