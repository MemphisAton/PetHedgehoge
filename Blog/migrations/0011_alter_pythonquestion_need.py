# Generated by Django 4.2.2 on 2023-07-12 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0010_pythonquestion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pythonquestion',
            name='need',
            field=models.BooleanField(default='True'),
        ),
    ]
