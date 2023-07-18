# Generated by Django 4.2.2 on 2023-07-18 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0013_category_englishwords_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='RulesOfEnglish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rules', models.CharField(max_length=255)),
                ('content', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='englishwords',
            name='rele',
            field=models.ManyToManyField(to='Blog.rulesofenglish'),
        ),
    ]
