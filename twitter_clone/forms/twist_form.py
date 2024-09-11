from django import forms
from ..models import Twist

class TwistForm(forms.ModelForm):
    body = forms.CharField(required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Enter Your Twist!!",
                "class": "form-control",
            }
        ),
        label="",
    )

    class Meta:
        model = Twist
        exclude = ('user',)