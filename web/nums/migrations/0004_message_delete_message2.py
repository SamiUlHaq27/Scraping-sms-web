# Generated by Django 5.0.2 on 2024-03-06 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nums', '0003_message2_delete_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=50)),
                ('at_time', models.DateTimeField(auto_now=True)),
                ('from_sndr', models.CharField(max_length=20)),
                ('text', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Message2',
        ),
    ]
