# Generated by Django 4.1 on 2022-08-30 22:16

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
                ('name', models.CharField(max_length=100)),
                ('start_year', models.CharField(max_length=4)),
                ('end_year', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Fads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.CharField(max_length=200, null=True)),
                ('description', models.CharField(default='No Description', max_length=200)),
                ('decade', models.CharField(max_length=100)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fads', to='nostaldja.decade')),
            ],
        ),
    ]
