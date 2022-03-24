# Generated by Django 3.2.9 on 2022-03-24 07:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FraudDetectCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Filename', models.CharField(max_length=100)),
                ('Percentage', models.FloatField(max_length=50)),
                ('FalsePos', models.IntegerField()),
                ('Suspicious', models.IntegerField()),
                ('NewCust', models.IntegerField()),
                ('DateTime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
