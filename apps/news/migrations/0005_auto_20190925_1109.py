# Generated by Django 2.2.4 on 2019-09-25 03:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20190925_1108'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='banner',
            options={'ordering': ['-priority']},
        ),
        migrations.RenameField(
            model_name='banner',
            old_name='position',
            new_name='priority',
        ),
    ]
