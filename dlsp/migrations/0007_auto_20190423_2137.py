# Generated by Django 2.2 on 2019-04-23 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dlsp', '0006_auto_20190423_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='media/images/%Y/%m/%d/'),
        ),
    ]
