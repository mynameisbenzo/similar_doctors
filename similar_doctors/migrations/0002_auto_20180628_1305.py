# Generated by Django 2.0.6 on 2018-06-28 20:05

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('similar_doctors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='type',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('HEART', 'CARDIOLOGIST'), ('GENERAL', 'GENERAL'), ('BRAIN', 'NEUROLOGIST'), ('EYE', 'OPTHALMOLOGIST'), ('EYE', 'OPTOMETRIST'), ('SKIN', 'DERMATOLOGIST'), ('MENTAL', 'PSYCHOLOGIST'), ('MENTAL', 'PSYCHIATRIST'), ('TEETH', 'DENTIST'), ('TEETH', 'ORTHODONIST'), ('COSMETIC', 'PLASTIC SURGEON')], max_length=67),
        ),
    ]
