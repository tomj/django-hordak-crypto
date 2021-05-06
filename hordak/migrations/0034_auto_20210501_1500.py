# Generated by Django 3.1.8 on 2021-05-01 15:00

from django.db import migrations
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('hordak', '0033_auto_20210501_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leg',
            name='amount_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('EUR', 'EURC'), ('ETH', 'Ethereum T'), ('SHIB', 'Shiba Token'), ('USD', 'USD $')], default='EUR', editable=False, max_length=20),
        ),
    ]