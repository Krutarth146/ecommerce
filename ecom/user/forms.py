from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegistrationForm(UserCreationForm):
    # email = forms.EmailField(label = 'E-mail',required=True)
 
    class Meta:
        model = User
        fields = {
            'first_name',
            'last_name',
            'username',
            'email',
            'phone',
            'password1',
            'password2'
        }

        # labels = {
        #     'last_name' : 'Last Name',
        #     'first_name' : 'Name'
        # }

    # def save(self,commit=True):
    #     user = super(RegistrationForm,self).save(commit=False)
    #     user.username = self.cleaned_data['username']
    #     user.first_name = self.cleaned_data['first_name']
    #     user.last_name = self.cleaned_data['last_name']
    #     user.email = self.cleaned_data['email']
    #     user.phone = self.cleaned_data['phone']
    #     user.password1 = self.cleaned_data['password1']
    #     user.password2 = self.cleaned_data['password2']

    #     if commit:
    #         user.save()
    #         user = User.objects.create(user = user)
    #         user.save()

    # def __init__(self, *args, **kwargs):
    #     super(RegistrationForm, self).__init__(*args, **kwargs)
    #     self.fields['username'].widget.attrs['class'] = 'form-control'
    #     self.fields['username'].widget.attrs['placeholder'] = 'Username'
    #     self.fields['first_name'].widget.attrs['class'] = 'form-control'
    #     self.fields['first_name'].widget.attrs['placeholder'] = 'First name'
    #     self.fields['last_name'].widget.attrs['class'] = 'form-control'
    #     self.fields['last_name'].widget.attrs['placeholder'] = 'Last name'
    #     self.fields['email'].widget.attrs['class'] = 'form-control'
    #     self.fields['email'].widget.attrs['placeholder'] = 'E-mail'
    #     self.fields['phone'].widget.attrs['class'] = 'form-control'
    #     self.fields['phone'].widget.attrs['placeholder'] = 'Phone Number'
    #     self.fields['password1'].widget.attrs['class'] = 'form-control'
    #     self.fields['password1'].widget.attrs['placeholder'] = 'Password'
    #     self.fields['password2'].widget.attrs['class'] = 'form-control'
    #     self.fields['password2'].widget.attrs['placeholder'] = 'Retype Password'