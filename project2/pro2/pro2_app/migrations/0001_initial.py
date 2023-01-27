# Generated by Django 4.0.4 on 2022-05-21 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=1000)),
                ('dateOfBirth', models.DateField()),
                ('GPA', models.DecimalField(decimal_places=2, max_digits=2)),
                ('level', models.CharField(max_length=500)),
                ('department', models.CharField(blank=True, max_length=500, null=True)),
                ('email', models.EmailField(max_length=250)),
                ('mobileNumber', models.CharField(max_length=250)),
            ],
        ),
    ]