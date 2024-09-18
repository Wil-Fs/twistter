from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UpdateProfileForm(forms.ModelForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Email Address"}))
    first_name = forms.CharField(label="", widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "First Name"}))
    last_name = forms.CharField(label="", widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Last Name"}))


    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',)



class UpdateDataProfileForm(UserCreationForm):
    email = forms.EmailField(label="Email", widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Email Address"}))
    usable_password = None
    usable_password_help_text = None


    class Meta:
        model = User
        fields = ('email', 'password1', 'password2',)
        exclude = ('username',)


    def __init__(self, *args, **kwargs):
        super(UpdateDataProfileForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
