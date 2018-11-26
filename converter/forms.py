from django import forms

from .models import Currency


class BalanceForm(forms.Form):
    balance = forms.DecimalField(max_digits=8, decimal_places=2)
    o_currency = forms.ModelChoiceField(queryset=Currency.objects.all())
    t_currency = forms.ModelChoiceField(queryset=Currency.objects.all())