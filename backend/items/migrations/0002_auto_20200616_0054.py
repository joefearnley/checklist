# Generated by Django 3.0.7 on 2020-06-16 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='content',
            new_name='description',
        ),
        migrations.AddField(
            model_name='item',
            name='complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='item',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='updated',
            field=models.DateField(auto_now=True),
        ),
    ]
