# Generated by Django 3.1.3 on 2020-11-08 09:50

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20201108_1022'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content2',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
