# Generated by Django 4.2.3 on 2023-07-09 06:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0004_alter_thing_user'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='thing',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='gear',
            name='category',
        ),
        migrations.RemoveField(
            model_name='gear',
            name='hash',
        ),
        migrations.RemoveField(
            model_name='gear',
            name='status',
        ),
        migrations.AddField(
            model_name='exercise',
            name='gear',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='api.gear'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gear',
            name='token_id',
            field=models.PositiveIntegerField(blank=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='gear',
            name='type',
            field=models.CharField(blank=True, choices=[('CAP', '帽子'), ('SHOES', '鞋子'), ('GLOVES', '手套')], max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='thing',
            name='level',
            field=models.CharField(blank=True, choices=[('BASIC', '初階'), ('INTERMEDIATE', '中階'), ('ADVANCED', '高階')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='gear',
            name='color',
            field=models.CharField(blank=True, choices=[('DARK', '暗色'), ('BRIGHT', '亮色'), ('COLORFUL', '彩色')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='gear',
            name='level',
            field=models.CharField(blank=True, choices=[('BASIC', '初階'), ('INTERMEDIATE', '中階'), ('ADVANCED', '高階')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='gear',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='thing',
            name='amount',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterUniqueTogether(
            name='thing',
            unique_together={('user', 'level')},
        ),
        migrations.RemoveField(
            model_name='thing',
            name='type',
        ),
    ]
