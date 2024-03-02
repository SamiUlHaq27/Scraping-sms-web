# Generated by Django 5.0.2 on 2024-03-01 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nums', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Number',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.SlugField(auto_created=True, default=models.CharField(max_length=50))),
                ('number', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=10)),
                ('active_since', models.CharField(max_length=20)),
                ('sms', models.IntegerField(default=0)),
                ('link', models.URLField()),
            ],
        ),
        migrations.AddField(
            model_name='country',
            name='url',
            field=models.SlugField(auto_created=True, default=models.CharField(max_length=50)),
        ),
    ]
