# Generated by Django 5.0.2 on 2024-03-04 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('link', models.URLField()),
                ('numbers', models.IntegerField(default=0)),
                ('slug_id', models.CharField(default='oops', max_length=50)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('flag', models.CharField(default='au', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=50)),
                ('at_time', models.CharField(max_length=20)),
                ('from_sndr', models.CharField(max_length=20)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Number',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=10)),
                ('active_since', models.CharField(max_length=20)),
                ('sms', models.IntegerField(default=0)),
                ('link', models.URLField()),
                ('slug_id', models.CharField(default='oops', max_length=50)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('country_flag', models.CharField(default='au', max_length=10)),
                ('country_slug', models.CharField(default='/', max_length=50)),
            ],
        ),
    ]
