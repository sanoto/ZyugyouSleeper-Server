# Generated by Django 2.0.2 on 2018-02-20 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moneymanager', '0009_auto_20180220_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='学籍番号'),
        ),
    ]
