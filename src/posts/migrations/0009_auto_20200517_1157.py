# Generated by Django 3.0.5 on 2020-05-17 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_article_is_english'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='overview',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='article',
            name='overview_ar',
            field=models.TextField(max_length=200),
        ),
    ]
