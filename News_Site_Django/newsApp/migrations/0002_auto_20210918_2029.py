# Generated by Django 3.2.7 on 2021-09-18 20:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='new',
            old_name='news_categort',
            new_name='news_category',
        ),
        migrations.AlterField(
            model_name='new',
            name='news_updateTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 18, 20, 29, 26, 968952)),
        ),
    ]