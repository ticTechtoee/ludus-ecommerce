from django import forms
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import MinLengthValidator
from django.core.validators import MinLengthValidator as MinLengthValidatorWidget
from .models import WebUser

class WebUserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'input-text input-text--primary-style',
            'placeholder': 'First Name'
        })
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'input-text input-text--primary-style',
            'placeholder': 'Last Name'
        })
    )
    BIRTH_MONTH_CHOICES = [
        ('', 'Month'),
        *[(str(i).zfill(2), datetime.strptime(str(i), '%m').strftime('%B')) for i in range(1, 13)]
    ]

    BIRTH_DAY_CHOICES = [
        ('', 'Day'),
        *[(str(i).zfill(2), str(i).zfill(2)) for i in range(1, 32)]
    ]

    current_year = datetime.now().year
    BIRTH_YEAR_CHOICES = [
        ('', 'Year'),
        *[(str(i), str(i)) for i in range(current_year, current_year - 100, -1)]
    ]

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    birth_month = forms.ChoiceField(choices=BIRTH_MONTH_CHOICES, widget=forms.Select(attrs={'class': 'select-box select-box--primary-style'}))
    birth_day = forms.ChoiceField(choices=BIRTH_DAY_CHOICES, widget=forms.Select(attrs={'class': 'select-box select-box--primary-style'}))
    birth_year = forms.ChoiceField(choices=BIRTH_YEAR_CHOICES, widget=forms.Select(attrs={'class': 'select-box select-box--primary-style'}))
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select(attrs={'class': 'select-box select-box--primary-style u-w-100'}))
    email = forms.EmailField(
        widget=forms.TextInput(attrs={
            'class': 'input-text input-text--primary-style',
            'placeholder': 'Enter E-mail',
        })
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'class': 'input-text input-text--primary-style',
            'placeholder': 'Enter Password',
        }),
        validators=[MinLengthValidator(limit_value=8)],
    )
    
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={
            'class': 'input-text input-text--primary-style',
            'placeholder': 'Re-enter Password',
        }),
    )

    class Meta:
        model = WebUser
        fields = ['first_name', 'last_name', 'email', 'birth_month', 'birth_day', 'birth_year', 'gender', 'password1', 'password2']
