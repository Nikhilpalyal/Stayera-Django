# Generated by Django 5.2 on 2025-04-14 18:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0005_remove_guest_first_name_remove_guest_last_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='guest',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='offers.guest'),
            preserve_default=False,
        ),
    ]
