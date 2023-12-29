# Generated by Django 4.2 on 2023-08-30 02:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("data_models", "0032_remove_land_area_use_purpose_landareausepurpose"),
    ]

    operations = [
        migrations.AddField(
            model_name="landareausepurpose",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, null=True, verbose_name="登録日時"
            ),
        ),
        migrations.AddField(
            model_name="landareausepurpose",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, null=True, verbose_name="更新日時"),
        ),
    ]
