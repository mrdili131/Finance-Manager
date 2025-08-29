from django import forms
from .models import Finance

class FinanceForm(forms.ModelForm):
    class Meta:
        model = Finance
        fields = ['amount','description','type','category']