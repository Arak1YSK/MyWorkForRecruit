# Generated by Django 4.2.1 on 2023-05-17 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("App_Folder", "0005_alter_status_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="account",
            name="status",
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name="Status",
        ),
    ]
