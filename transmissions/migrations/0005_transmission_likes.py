# Generated by Django 3.1.7 on 2021-03-11 17:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('transmissions', '0004_auto_20210310_1035'),
    ]

    operations = [
        migrations.AddField(
            model_name='transmission',
            name='likes',
            field=models.ManyToManyField(related_name='transmission_like', to=settings.AUTH_USER_MODEL),
        ),
    ]