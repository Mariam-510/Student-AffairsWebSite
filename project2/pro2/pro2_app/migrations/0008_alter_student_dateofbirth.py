# Generated by Django 4.0.4 on 2022-05-24 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pro2_app', '0007_alter_student_dateofbirth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='dateOfBirth',
            field=models.DateField(),
        ),
    ]
