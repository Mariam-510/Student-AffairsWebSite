# Generated by Django 4.0.4 on 2022-05-21 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pro2_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='GPA',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]