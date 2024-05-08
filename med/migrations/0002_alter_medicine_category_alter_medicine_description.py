# Generated by Django 5.0.1 on 2024-05-08 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('med', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='category',
            field=models.CharField(choices=[('Ayurveda', 'Ayurveda'), ('Allopathy', 'Allopathy'), ('Homeopathy', 'Homeopathy')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='description',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
