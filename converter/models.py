from django.db.models import *


class Currency(Model):
    currency = CharField(max_length=3)

    def __str__(self):
        return self.currency

class ExchangeRate(Model):
    o_currency = ForeignKey(Currency, on_delete=PROTECT, related_name='o_currency')
    t_currency = ForeignKey(Currency, on_delete=PROTECT, related_name='t_currency')
    rate = DecimalField(max_digits=6, decimal_places=4)

    def __str__(self):
        return '{}, {}'.format(self.o_currency, self.t_currency)