# Generated by Django 3.1.7 on 2021-03-07 19:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_auto_20210307_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='next_review_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 7, 19, 6, 56, 949518, tzinfo=utc)),
        ),
    ]
