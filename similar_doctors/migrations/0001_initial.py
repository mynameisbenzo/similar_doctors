# Generated by Django 2.0.6 on 2018-06-28 19:59

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('type', multiselectfield.db.fields.MultiSelectField(choices=[('CARDIOLOGIST', 'HEART'), ('GENERAL', 'GENERAL'), ('NEUROLOGIST', 'BRAIN'), ('OPTHALMOLOGIST', 'EYE'), ('OPTOMETRIST', 'EYE'), ('DERMATOLOGIST', 'SKIN'), ('PSYCHOLOGIST', 'MENTAL'), ('PSYCHIATRIST', 'MENTAL'), ('DENTIST', 'TEETH'), ('ORTHODONIST', 'TEETH'), ('PLASTIC SURGEON', 'COSMETIC')], max_length=135)),
            ],
        ),
    ]