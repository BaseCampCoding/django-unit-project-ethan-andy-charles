# Generated by Django 3.1.7 on 2021-03-10 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transmissions', '0003_auto_20210310_1026'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='authhor',
            new_name='author',
        ),
    ]