from django import forms
from .models import Review


class AppointmentForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label='Name',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Name',
                'id': 'name',
            }
        )
    )
    phone_number = forms.CharField(
        max_length=15,
        label='Phone number',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Phone number',
                'id': 'phone_number',
            }
        )
    )
    services = forms.ChoiceField(
        choices=[
            ('', 'Select Your Object'),
            ('Office', 'Office'),
            ('Apartment', 'Apartment'),
            ('House', 'House'),
        ],
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'object',
            }
        )
    )
    cleaner = forms.ChoiceField(
        choices=[
            ('', 'Select Date'),
            ('John Doe', 'John Doe'),
            ('William Smith', 'William Smith'),
            ('Danny Green', 'Danny Green'),
            ('Jason Thompson', 'Jason Thompson')
        ],
        label='Cleaner',
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'cleaner',
            }
        )
    )


class ReviewAdminForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['id', 'name', 'date', 'feedback']
