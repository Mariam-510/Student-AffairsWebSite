# Generated by Django 4.0.4 on 2022-05-22 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pro2_app', '0004_alter_student_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=250),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=250),
        ),
    ]
