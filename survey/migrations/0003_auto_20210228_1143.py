# Generated by Django 3.1.6 on 2021-02-28 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_auto_20210228_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='option1',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='choice',
            name='option2',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='choice',
            name='question',
            field=models.CharField(max_length=100),
        ),
    ]