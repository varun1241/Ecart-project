from .models import Product
from django import forms

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('product_name','price','strap_color','highlights','image','status')

        widget ={
            'product_name':forms.TextInput(attrs={'class':'form-control'}),
             'price':forms.TextInput(attrs={'class':'form-control'}),
              'strap_color':forms.TextInput(attrs={'class':'form-control'}),
               'highlights':forms.TextInput(attrs={'class':'form-control'}),
                'image':forms.ImageField(),
                 'status':forms.BooleanField( )

        }