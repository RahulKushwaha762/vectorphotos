# Generated by Django 3.0.2 on 2020-02-10 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0008_auto_20200209_0946'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='image',
        ),
        migrations.AddField(
            model_name='images',
            name='imgpicture',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]