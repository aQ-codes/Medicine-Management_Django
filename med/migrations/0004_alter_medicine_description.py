# Generated by Django 5.0.1 on 2024-05-18 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('med', '0003_alter_medicine_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='description',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
