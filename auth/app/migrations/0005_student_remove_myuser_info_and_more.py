# Generated by Django 4.2.5 on 2023-10-03 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0004_alter_student_info_photo"),
    ]

    operations = [
        migrations.CreateModel(
            name="student",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=30)),
                ("last_name", models.CharField(max_length=30)),
                ("gender", models.CharField(max_length=4)),
                ("age", models.IntegerField(default=0)),
                ("branch", models.CharField(max_length=30)),
                ("semester", models.CharField(max_length=2)),
                ("divison", models.CharField(max_length=1)),
                ("address", models.CharField(max_length=30)),
                ("photo", models.FileField(upload_to="auth/files/profiles")),
                ("grade", models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name="myuser",
            name="info",
        ),
        migrations.AlterField(
            model_name="certificates",
            name="certificate",
            field=models.FileField(upload_to="auth/certificates"),
        ),
        migrations.AlterField(
            model_name="internships",
            name="internship",
            field=models.FileField(upload_to="auth/files/internships"),
        ),
        migrations.AlterField(
            model_name="reports",
            name="repot",
            field=models.FileField(upload_to="auth/files/repots"),
        ),
        migrations.AddField(
            model_name="myuser",
            name="student",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="app.student",
            ),
        ),
        migrations.AlterField(
            model_name="certificates",
            name="key",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="app.student",
            ),
        ),
        migrations.AlterField(
            model_name="internships",
            name="key",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="app.student",
            ),
        ),
        migrations.AlterField(
            model_name="reports",
            name="key",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="app.student",
            ),
        ),
        migrations.DeleteModel(
            name="student_info",
        ),
    ]
