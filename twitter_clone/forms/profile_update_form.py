from django import forms
from ..models import Profile


class ProfilePicForm(forms.ModelForm):
    profile_image = forms.ImageField(label='Profile Picture', widget=forms.FileInput(attrs={
        "class":"form-control"
    }))
    profile_background = forms.ImageField(label='Profile Picture', widget=forms.FileInput(attrs={
        "class": "form-control"
    }))
    bio = forms.CharField(label="Profile bio", widget=forms.Textarea(attrs={
        "class":"form-control",
        "placeholder":"Tell more about you."
    }))

    class Meta:
        model = Profile
        fields = ('profile_image', 'profile_background', 'bio',)