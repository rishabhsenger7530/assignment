# Generated by Django 4.0 on 2021-12-14 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BuildingInfo',
            fields=[
                ('buildingId', models.PositiveIntegerField(primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]