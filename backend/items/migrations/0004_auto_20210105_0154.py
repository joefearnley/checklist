# Generated by Django 3.0.7 on 2021-01-05 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_auto_20200818_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='due_date',
            field=models.DateField(null=True),
        ),
    ]
