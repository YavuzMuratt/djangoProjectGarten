# Generated by Django 5.1 on 2024-08-30 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("registration", "0003_alter_student_father_phone"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="points",
            field=models.IntegerField(),
        ),
    ]
