# Generated by Django 4.0.4 on 2022-05-24 12:46

from django.db import migrations, models
import pro2_app.validators


class Migration(migrations.Migration):

    dependencies = [
        ('pro2_app', '0014_alter_student_gender_alter_student_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=250, validators=[pro2_app.validators.validate_domainonly_email]),
        ),
    ]
