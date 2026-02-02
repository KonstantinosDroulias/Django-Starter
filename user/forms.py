from django import forms
from .models import Profile

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'phone_number']
        widgets = {
            'bio': forms.Textarea(attrs={
                'class': 'textarea textarea-bordered w-full bg-base-100',
                'rows': 4,
                'placeholder': 'Tell us about yourself...'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'input input-bordered w-full bg-base-100',
                'placeholder': 'e.g. +30 210...'
            }),
            'avatar': forms.FileInput(attrs={
                'class': 'file-input file-input-bordered file-input-primary w-full bg-base-100'
            }),
        }