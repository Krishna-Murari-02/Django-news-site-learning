# Generated by Django 3.2.7 on 2021-09-20 17:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsApp', '0004_alter_new_news_updatetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='news_updateTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 20, 17, 53, 48, 678137)),
        ),
    ]
