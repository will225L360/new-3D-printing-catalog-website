# Generated by Django 4.2.4 on 2023-09-07 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_image_up_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='prod_name',
            field=models.CharField(default=None, max_length=150),
        ),
    ]