# Generated by Django 4.2.2 on 2023-07-11 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0005_englishwords'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnglishRules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rules', models.CharField(max_length=255)),
                ('content', models.CharField(max_length=255)),
            ],
        ),
    ]
