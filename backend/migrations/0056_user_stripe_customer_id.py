# Generated by Django 5.1 on 2024-08-29 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0055_remove_planfeature_group_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="stripe_customer_id",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]