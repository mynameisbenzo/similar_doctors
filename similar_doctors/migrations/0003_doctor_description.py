# Generated by Django 2.0.6 on 2018-06-28 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('similar_doctors', '0002_auto_20180628_1305'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='description',
            field=models.CharField(default='A great doctor.', max_length=500),
        ),
    ]
