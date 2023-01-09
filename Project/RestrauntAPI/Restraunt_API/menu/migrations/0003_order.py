# Generated by Django 3.2.7 on 2022-06-01 12:01

from django.db import migrations, models
import menu.models


class Migration(migrations.Migration):

    dependencies = [
        ("menu", "0002_alter_menu_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
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
                (
                    "email",
                    models.EmailField(max_length=60, unique=True, verbose_name="email"),
                ),
                ("Item_name", models.CharField(max_length=100)),
                (
                    "Image",
                    models.ImageField(default="", upload_to=menu.models.upload_to),
                ),
                ("Price", models.FloatField()),
                ("Discount", models.FloatField()),
                ("Plate_size", models.IntegerField()),
                ("zip_code", models.IntegerField(max_length=6)),
                ("Address", models.TextField()),
                ("order_time", models.DateTimeField()),
                ("sts", models.CharField(default=None, max_length=50)),
            ],
        ),
    ]
