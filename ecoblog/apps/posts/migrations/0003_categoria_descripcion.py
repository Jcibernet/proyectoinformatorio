# Generated by Django 3.0 on 2021-12-13 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='descripcion',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
