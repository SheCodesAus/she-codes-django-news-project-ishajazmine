# Generated by Django 4.0.1 on 2022-02-19 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_newsstory_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsstory',
            name='image',
            field=models.URLField(blank=True, null=True),
        ),
    ]
