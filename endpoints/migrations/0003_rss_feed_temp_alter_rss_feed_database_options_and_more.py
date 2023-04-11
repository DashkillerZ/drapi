# Generated by Django 4.1.7 on 2023-03-07 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endpoints', '0002_rss_feed_url_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RSS_Feed_Temp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedName', models.TextField()),
                ('title', models.TextField()),
                ('publishedDate', models.DateTimeField()),
                ('link', models.TextField()),
                ('summary', models.TextField()),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles(Discarded)',
            },
        ),
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
        migrations.AlterField(
            model_name='rss_feed_database',
            name='publishedDate',
            field=models.DateTimeField(),
        ),
    ]
