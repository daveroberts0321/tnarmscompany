# Generated by Django 4.0.4 on 2022-10-25 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='isfeatured',
            field=models.BooleanField(default=True),
        ),
    ]
