# Generated by Django 2.0.2 on 2018-02-20 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moneymanager', '0005_auto_20180220_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.IntegerField(default=3, primary_key=True, serialize=False, verbose_name='学籍番号'),
        ),
    ]
