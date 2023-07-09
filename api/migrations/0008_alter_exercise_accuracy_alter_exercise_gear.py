# Generated by Django 4.2.3 on 2023-07-09 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_remove_exercise_type_alter_gear_level_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='accuracy',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='gear',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.gear'),
        ),
    ]
