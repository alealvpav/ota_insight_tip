# Generated by Django 3.2.14 on 2022-07-11 21:17

from django.db import migrations
import shortuuid.django_fields


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='number',
            field=shortuuid.django_fields.ShortUUIDField(alphabet='0123456789', length=5, max_length=9, prefix='OTA-', unique=True),
        ),
    ]
