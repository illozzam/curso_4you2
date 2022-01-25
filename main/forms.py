from django import forms
from django.core.exceptions import ValidationError

from main.models import Produto


NUMBER_WIDGET = forms.NumberInput(attrs={'class': 'form-control'})

class CarrinhoForm(forms.ModelForm):
    # quantidade = forms.IntegerField(min_value=1, widget=NUMBER_WIDGET)
    # preco = forms.DecimalField(max_digits=10, decimal_places=2, widget=NUMBER_WIDGET)
    class Meta:
        model = Produto
        fields = ['quantidade', 'preco']
        widgets = {
            'quantidade': NUMBER_WIDGET,
            'preco': NUMBER_WIDGET,
        }