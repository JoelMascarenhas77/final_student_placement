# Generated by Django 4.2.5 on 2023-10-04 14:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0006_alter_certificates_certificate_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="photo",
            field=models.FileField(upload_to="profiles"),
        ),
    ]