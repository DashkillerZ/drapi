# Generated by Django 4.1.7 on 2023-02-24 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endpoints', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RSS_Feed_URL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedUrl', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='rss_feed_database',
            old_name='Summary',
            new_name='summary',
        ),
    ]
