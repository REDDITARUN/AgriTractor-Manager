from django import forms 
from .models import Tractor



class TractorForm(forms.ModelForm):
  class Meta:
    model = Tractor
    fields = ['tractor_id', 'model_name', 'owner_name', 'email', 'field_Implements', 'used_by']
    labels = {
      'tractor_id': 'Tractor Number', 
      'model_name': 'Model Name', 
      'owner_name': 'Owner Name', 
      'email': 'Email', 
      'field_Implements': 'Implements', 
      'used_by': 'USED BY'
    }
    widgets = {
      'tractor_id': forms.NumberInput(attrs={'class': 'form-control'}), 
      'model_name': forms.TextInput(attrs={'class': 'form-control'}),
      'owner_name': forms.TextInput(attrs={'class': 'form-control'}),
      'email': forms.EmailInput(attrs={'class': 'form-control'}),
      'field_Implements': forms.Select(attrs={'class': 'form-control'}),
      'used_by': forms.NumberInput(attrs={'class': 'form-control'}),
    }