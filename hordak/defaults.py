from django.conf import settings

import moneyed

INTERNAL_CURRENCY = getattr(settings, "HORDAK_INTERNAL_CURRENCY", "EUR")

DEFAULT_CURRENCY = getattr(settings, "DEFAULT_CURRENCY", "EUR")

CURRENCIES = getattr(settings, "CURRENCIES", ["SHIB", "ETH"])

DECIMAL_PLACES = getattr(settings, "HORDAK_DECIMAL_PLACES", 15)

MAX_DIGITS = getattr(settings, "HORDAK_MAX_DIGITS", 30)

CURRENCY_CODE_MAX_LENGTH = 20


# TODO: make this pull from a DB or something similar, it must be dynamic
class Setup:
    @staticmethod
    def add_custom_currencies():
        moneyed.add_currency("ADA", "000", "Cardano", None)
        moneyed.add_currency("BTC", "000", "Bitcoin", None)
        moneyed.add_currency("COMP", "000", "Compound", None)
        moneyed.add_currency("DAI", "000", "Dai", None)
        moneyed.add_currency("DEFI5", "000", "defi5", None)
        moneyed.add_currency("ETH", "000", "Ethereum", None)
        moneyed.add_currency("KRILL", "000", "Krill", None)
        moneyed.add_currency("LEASH", "000", "Leash", None)
        moneyed.add_currency("MATIC", "000", "Polygon", None)
        moneyed.add_currency("NANO", "000", "Nano", None)
        moneyed.add_currency("SHIB", "000", "Shiba Token", None)
        moneyed.add_currency("TRX", "000", "TRON", None)
        moneyed.add_currency("USDT", "000", "Tether", None)
