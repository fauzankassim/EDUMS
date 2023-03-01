from django import forms
from .models import Item

class AddItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ['name', 'image', 'description', 'quantity', 'price']


class BuyItemForm(forms.Form):

    quantity = forms.IntegerField(min_value=1)


    
