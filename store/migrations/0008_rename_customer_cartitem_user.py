# Generated by Django 4.0.4 on 2022-11-10 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_cartitem_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='customer',
            new_name='user',
        ),
    ]
