# Generated by Django 4.2 on 2023-05-03 11:47

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("advert", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="advert",
            options={
                "ordering": ["-created_at"],
                "verbose_name": "Объявление",
                "verbose_name_plural": "Объявления",
            },
        ),
    ]