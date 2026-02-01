from .models import shop
from django import forms

class UpdateForm(forms.ModelForm):
    class Meta:
        model=shop
        fields=['name','desc','price','img','category']
    print("Updated Successfully....")