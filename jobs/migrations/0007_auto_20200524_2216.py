# Generated by Django 2.2.6 on 2020-05-24 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_auto_20200524_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(default='', null=True, upload_to=''),
        ),
    ]