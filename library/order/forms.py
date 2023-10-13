from django import forms

from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['book', 'user', 'end_at']
        labels = {'book': 'book', 'user': 'user', 'end_at': 'end_at'}