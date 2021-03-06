# Generated by Django 3.0.6 on 2021-03-23 06:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210322_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gainlosschartdata',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 23, 12, 12, 56, 74526), null=True),
        ),
        migrations.AlterField(
            model_name='gainlosshistory',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 23, 12, 12, 56, 73972), null=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 23, 12, 12, 56, 71928), null=True),
        ),
        migrations.AlterField(
            model_name='stocknames',
            name='name',
            field=models.TextField(blank=True, db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='totalgainloss',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 23, 12, 12, 56, 73545), null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 23, 12, 12, 56, 71081), null=True),
        ),
        migrations.AlterField(
            model_name='transactionhistory',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 23, 12, 12, 56, 73187), null=True),
        ),
    ]
