# Generated by Django 2.2.4 on 2020-02-09 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0007_images_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to=''),
        ),
    ]
