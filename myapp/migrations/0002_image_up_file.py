# Generated by Django 4.2.4 on 2023-09-07 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='up_file',
            field=models.FileField(default=None, upload_to='myfile'),
        ),
    ]