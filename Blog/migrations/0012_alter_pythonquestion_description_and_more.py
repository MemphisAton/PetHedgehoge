# Generated by Django 4.2.2 on 2023-07-12 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0011_alter_pythonquestion_need'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pythonquestion',
            name='description',
            field=models.TextField(blank=True, null='True'),
        ),
        migrations.AlterField(
            model_name='pythonquestion',
            name='need',
            field=models.BooleanField(default=False),
        ),
    ]
