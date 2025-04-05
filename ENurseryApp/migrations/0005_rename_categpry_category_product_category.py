# Generated by Django 5.1.6 on 2025-04-02 17:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ENurseryApp', '0004_categpry'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categpry',
            new_name='Category',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ENurseryApp.category'),
        ),
    ]
