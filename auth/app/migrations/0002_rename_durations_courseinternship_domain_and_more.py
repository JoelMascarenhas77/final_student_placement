# Generated by Django 4.2.6 on 2023-10-15 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courseinternship',
            old_name='durations',
            new_name='domain',
        ),
        migrations.RemoveField(
            model_name='courseinternship',
            name='grade',
        ),
        migrations.AddField(
            model_name='courseinternship',
            name='duration',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Placement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('salary', models.IntegerField()),
                ('position', models.CharField(max_length=100)),
                ('placement_type', models.CharField(choices=[('incampus', 'In Campus Placement'), ('outside', 'Outside Placement')], default='incampus', max_length=10)),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.student')),
            ],
        ),
    ]
