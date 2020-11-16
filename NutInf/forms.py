from django import forms
from .models import Nutinf, Products

class NutinfForm(forms.ModelForm):
    class Meta:
        model=Nutinf
        fields=['name','unit']
        
        widgets={
            'name': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Energy value',
                    }
                ),
            'unit': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Unit of measure',
                    }
                )

            }

class ProductsForm(forms.ModelForm):
    class Meta:
        model=Products
        fields=['name_product', 'description', 'nutval', 'active']