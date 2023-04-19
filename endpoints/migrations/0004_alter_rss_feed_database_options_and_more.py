# Generated by Django 4.1.7 on 2023-03-05 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('endpoints', '0003_alter_rss_feed_database_publisheddate'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rss_feed_database',
            options={'verbose_name': 'Article', 'verbose_name_plural': 'Articles'},
        ),
        migrations.AlterModelOptions(
            name='rss_feed_keyowrds',
            options={'verbose_name': 'Keyword', 'verbose_name_plural': 'Keywords'},
        ),
        migrations.AlterModelOptions(
            name='rss_feed_name_icon',
            options={'verbose_name': 'Feed', 'verbose_name_plural': 'Feeds'},
        ),
        migrations.AlterModelOptions(
            name='rss_feed_url',
            options={'verbose_name': 'URL', 'verbose_name_plural': 'URLs'},
        ),
    ]
