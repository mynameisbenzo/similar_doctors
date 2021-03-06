# Generated by Django 2.0.6 on 2018-06-28 22:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('similar_doctors', '0004_auto_20180628_1339'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], max_length=2)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='similar_doctors.Doctor')),
            ],
        ),
    ]
