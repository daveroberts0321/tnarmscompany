# Generated by Django 4.0.4 on 2022-10-26 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_isfeatured'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='category',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='mainimg',
            field=models.ImageField(blank=True, default='images/default.jpg', null=True, upload_to='images/', verbose_name='Main Category Image'),
        ),
        migrations.AddField(
            model_name='category',
            name='subtext',
            field=models.TextField(blank=True, null=True),
        ),
    ]
