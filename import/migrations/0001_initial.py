# Generated by Django 3.1.2 on 2020-10-08 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PatientInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default=None, max_length=50)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('hospital', models.CharField(blank=True, max_length=50, null=True)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=16)),
            ],
        ),
    ]
