from django.forms.models import ModelForm
from .models import Expense


class expense_add(ModelForm):
    class Meta:
        model = Expense
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(expense_add, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'style': 'color: white'
        })
