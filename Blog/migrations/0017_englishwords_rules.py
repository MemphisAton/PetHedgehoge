# Generated by Django 4.2.2 on 2023-07-18 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0016_remove_englishwords_rules'),
    ]

    operations = [
        migrations.AddField(
            model_name='englishwords',
            name='rules',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
