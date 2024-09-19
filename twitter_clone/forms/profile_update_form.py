from django import forms
from ..models import Profile


class ProfilePicForm(forms.ModelForm):
    profile_image = forms.ImageField(label='Profile Picture', required=False, widget=forms.FileInput(attrs={
        "class":"form-control"
    }))
    bio = forms.CharField(label="Profile bio", required=False, widget=forms.Textarea(attrs={
        "class":"form-control",
        "placeholder":"Tell more about you."
    }))

    class Meta:
        model = Profile
        fields = ('profile_image', 'bio',)



class ProfileCoverForm(forms.ModelForm):

    profile_background = forms.ImageField(label='Profile Cover', required=False, widget=forms.FileInput(attrs={
        "class": "form-control"
    }))


    class Meta:
        model = Profile
        fields = ('profile_background',)