# Generated by Django 4.1 on 2022-08-30 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Decade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='no decade name', max_length=100)),
                ('start_year', models.CharField(default='no decade start year', max_length=100)),
                ('end_year', models.CharField(default='no decade end year', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Fad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='no fad name', max_length=100)),
                ('image_url', models.CharField(max_length=100, null=True)),
                ('description', models.CharField(default='no fad description', max_length=100)),
                ('decade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Fads', to='nostaldja.decade')),
            ],
        ),
    ]
