# Generated by Django 4.2.19 on 2025-03-06 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_categroy_id_sub_category_categroy'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sub_category',
            old_name='categroy',
            new_name='categroy_id',
        ),
    ]
