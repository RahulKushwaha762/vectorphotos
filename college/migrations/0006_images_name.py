# Generated by Django 3.0.2 on 2020-02-07 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0005_auto_20200207_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
