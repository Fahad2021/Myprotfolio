# Generated by Django 4.1.1 on 2022-09-18 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainapp',
            name='image',
            field=models.FilePathField(path='D:/python+django/Myprotfolio/myprotfolio/mainapp/static/img'),
        ),
    ]
