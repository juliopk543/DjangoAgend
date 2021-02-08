# Generated by Django 3.1.5 on 2021-02-08 15:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0003_auto_20210123_2252'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='foto',
            field=models.ImageField(blank=True, upload_to='foto/%Y/%m/'),
        ),
        migrations.AlterField(
            model_name='contato',
            name='data_criacao',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 8, 15, 13, 38, 626963, tzinfo=utc)),
        ),
    ]