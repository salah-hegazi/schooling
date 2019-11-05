# Generated by Django 2.2.3 on 2019-11-05 06:06

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20191030_0428'),
    ]

    operations = [
        migrations.AddField(
            model_name='managerialemployee',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(default='', max_length=128, region=None, unique=True, verbose_name='Phone number of Employee'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parent',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(default='', max_length=128, region=None, unique=True, verbose_name='Phone number of Parent'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(default='', max_length=128, region=None, unique=True, verbose_name='Phone number of Teacher'),
            preserve_default=False,
        ),
    ]
