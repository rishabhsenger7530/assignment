# Generated by Django 4.0 on 2021-12-14 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0004_uploadmeterinfo_meterdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='HourlyConsumption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consumption', models.FloatField()),
                ('reading_date_time', models.DateTimeField()),
                ('meter_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.meterdata')),
            ],
        ),
    ]