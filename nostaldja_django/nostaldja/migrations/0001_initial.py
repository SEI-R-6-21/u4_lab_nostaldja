# Generated by Django 4.1 on 2022-08-31 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fad_name', models.CharField(max_length=100)),
                ('fad_type', models.CharField(max_length=100)),
                ('photo_url', models.TextField(max_length=200)),
                ('fad_phrase', models.CharField(max_length=100)),
            ],
        ),
    ]
