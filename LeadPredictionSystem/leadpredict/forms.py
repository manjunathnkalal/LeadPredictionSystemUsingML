from django import forms
from .models import Inputmodel

class Inputform(forms.ModelForm):
    class Meta:
        model = Inputmodel
        fields = [
            'total_visits', 
            'total_time_spent_on_website', 
            'page_views_per_visit', 
            'lead_origin', 
            'lead_source', 
            'last_activity', 
            'specialization', 
            'current_occupation', 
            'tags', 
            'lead_quality', 
            'city', 
            'do_not_email', 
            'last_notable_activity', 
            'free_copy_of_mastering_the_interview', 
        ]

        widgets = {
            'lead_origin': forms.Select(attrs={'class': 'form-control'}),
            'lead_source': forms.Select(attrs={'class': 'form-control'}),
            'last_activity': forms.Select(attrs={'class': 'form-control'}),
            'specialization': forms.Select(attrs={'class': 'form-control'}),
            'current_occupation': forms.Select(attrs={'class': 'form-control'}),
            'tags': forms.Select(attrs={'class': 'form-control'}),
            'lead_quality': forms.Select(attrs={'class': 'form-control'}),
            'city': forms.Select(attrs={'class': 'form-control'}),
            'do_not_email': forms.Select(attrs={'class': 'form-check-input'}),
            'last_notable_activity': forms.Select(attrs={'class': 'form-control'}),
            'free_copy_of_mastering_the_interview': forms.Select(attrs={'class': 'form-check-input'}),
            'total_visits': forms.NumberInput(attrs={'class': 'form-control'}),
            'total_time_spent_on_website': forms.NumberInput(attrs={'class': 'form-control'}),
            'page_views_per_visit': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(Inputform, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = True  # Set each field as required
