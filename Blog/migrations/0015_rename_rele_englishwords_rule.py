# Generated by Django 4.2.2 on 2023-07-18 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0014_rulesofenglish_englishwords_rele'),
    ]

    operations = [
        migrations.RenameField(
            model_name='englishwords',
            old_name='rele',
            new_name='rule',
        ),
    ]
