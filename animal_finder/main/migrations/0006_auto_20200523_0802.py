# Generated by Django 3.0.4 on 2020-05-23 11:02

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200522_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='foto',
            field=models.ImageField(upload_to=main.models.UploadToPathAndRename('2020_05_23_')),
        ),
    ]
