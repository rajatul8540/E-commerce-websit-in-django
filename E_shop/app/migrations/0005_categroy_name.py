# Generated by Django 4.2.19 on 2025-03-06 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_categroy_sub_category_categroy_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='categroy',
            name='name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
