# Generated by Django 5.0.6 on 2024-05-31 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fresh_news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['publish_date'], 'verbose_name': 'News', 'verbose_name_plural': 'News'},
        ),
    ]
