from django import forms
from .models import *

class supplier_form(forms.ModelForm):
    class Meta:
        model = supplier
        fields=['Address','city','state','country','Pincode']
        widgets={

            'Address': forms.TextInput(attrs={'class': 'form-control','placeholder':'Address'}),
            'city': forms.TextInput(attrs={'class': 'form-control','placeholder':'city'}),
            'state': forms.TextInput(attrs={'class': 'form-control','placeholder':'state'}),
            'country': forms.TextInput(attrs={'class': 'form-control','placeholder':'country'}),
            'Pincode': forms.TextInput(attrs={'class': 'form-control','placeholder':'Pincode'}),
        }