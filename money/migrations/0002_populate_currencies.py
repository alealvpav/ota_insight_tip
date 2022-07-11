from django.db import migrations
from money.utils.currency_default_data import get_currency_data


def populate_currencies(apps, schema_editor):
    Currency = apps.get_model('money', 'Currency')
    currency_dict = get_currency_data()
    for currency in currency_dict:
        Currency.objects.create(**currency)


class Migration(migrations.Migration):

    dependencies = [
        ('money', '0001_initial'),
    ]

    operations = [
      migrations.RunPython(populate_currencies),
    ]
