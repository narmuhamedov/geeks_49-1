# Generated by Django 5.1.5 on 2025-02-08 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tv_show', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='filmmodel',
            options={'verbose_name': 'фильм', 'verbose_name_plural': 'фильмы'},
        ),
        migrations.AddField(
            model_name='filmmodel',
            name='music',
            field=models.FileField(blank=True, null=True, upload_to='music/', verbose_name='Загрузите музыку'),
        ),
    ]
