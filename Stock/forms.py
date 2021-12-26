from django.forms.models import ModelForm
from .models import Inventory, Product


class Inventory_Add(ModelForm):
    class Meta:
        model = Inventory
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(Inventory_Add, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'style': 'color: white'
        })


class Product_Add(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(Product_Add, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'style': 'color: white'
        })
