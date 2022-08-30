from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Decade",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("start_year", models.CharField(max_length=20)),
                ("end_year", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="Fad",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("img_url", models.CharField(max_length=200, null=True)),
                ("description", models.TextField(max_length=200)),
                (
                    "decade",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="fad",
                        to="nostaldja_app.decade",
                    ),
                ),
            ],
        ),
    ]
