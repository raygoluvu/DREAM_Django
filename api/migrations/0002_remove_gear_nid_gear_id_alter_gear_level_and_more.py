# Generated by Django 4.2.3 on 2023-07-09 03:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="gear",
            name="nid",
        ),
        migrations.AddField(
            model_name="gear",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="gear",
            name="level",
            field=models.IntegerField(
                blank=True, choices=[(1, "Low"), (2, "Mid"), (3, "High")], null=True
            ),
        ),
        migrations.AlterModelTable(
            name="gear",
            table="gear",
        ),
        migrations.AlterModelTable(
            name="thing",
            table="thing",
        ),
    ]
