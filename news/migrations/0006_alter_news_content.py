# Generated by Django 4.0.5 on 2022-07-11 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_alter_news_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='content',
            field=models.TextField(blank=True, verbose_name='Контент'),
        ),
    ]
