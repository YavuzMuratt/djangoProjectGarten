# Generated by Django 5.1 on 2024-08-30 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("registration", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="mother_phone",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="student",
            name="name",
            field=models.CharField(max_length=64),
        ),
    ]
