# Generated by Django 4.2.3 on 2023-07-10 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gear',
            name='work_max',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
