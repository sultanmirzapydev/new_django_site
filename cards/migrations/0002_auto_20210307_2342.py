# Generated by Django 3.1.7 on 2021-03-07 18:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='next_review_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 7, 18, 12, 58, 903342, tzinfo=utc)),
        ),
    ]
