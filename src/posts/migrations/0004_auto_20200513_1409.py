# Generated by Django 3.0.6 on 2020-05-13 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20200513_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='is_feautred',
            field=models.BooleanField(default=False),
        ),
    ]
