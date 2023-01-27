# Generated by Django 4.0.4 on 2022-05-22 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pro2_app', '0005_student_status_alter_student_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.CharField(blank=True, choices=[('Computer Science (CS)', 'Computer Science (CS)'), ('Artificial Intelligence (AI)', 'Artificial Intelligence (AI)'), ('Information Technology (IT)', 'Information Technology (IT)'), ('Information System (IS)', 'Information System (IS)'), ('Decision Support (DS)', 'Decision Support (DS)')], max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='level',
            field=models.CharField(choices=[('First Level', 'First Level'), ('Second Level', 'Second Level'), ('Third Level', 'Third Level'), ('Fourth Level', 'Fourth Level')], max_length=500),
        ),
    ]
