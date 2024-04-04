from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class CreateUserForm(UserCreationForm):


    class Meta:
        model=User
        fields=['username','email','password1','password2']

    #def clean_password2(self):
        #cd = self.cleaned_data
        #if cd['password'] != cd['password2']:
          # raise forms.ValidationError('Passwords don\'t match.')
        #return cd['password2']

class SalaryForm(forms.Form):
    basic_salary = forms.DecimalField(label='Basic Salary', max_digits=10, decimal_places=2, required=False)
    payment_rate = forms.DecimalField(label='Rate per Hour', max_digits=10, decimal_places=2, required=False)
    bonus = forms.DecimalField(label='Bonus', max_digits=10, decimal_places=2, required=False)
    deduction = forms.DecimalField(label='Deduction', max_digits=10, decimal_places=2, required=False)
    # Add more fields as needed
