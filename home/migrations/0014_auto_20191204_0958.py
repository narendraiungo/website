# Generated by Django 2.2.7 on 2019-12-04 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20191203_1217'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='username',
            new_name='con_password',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='mobile_phone',
            new_name='phone_number',
        ),
    ]
