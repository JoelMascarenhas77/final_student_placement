# Generated by Django 4.2.6 on 2023-10-16 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_prediction_gender_alter_prediction_hostel_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='prediction',
            name='internship',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
