# Generated by Django 5.0.2 on 2024-02-29 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_habit_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='action',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='действие'),
        ),
    ]