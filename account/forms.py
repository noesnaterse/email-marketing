from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["email"].widget.attrs["placeholder"] = "e-mail address"
        self.fields["email"].widget.attrs["class"] = "block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
        self.fields["email"].label_classes = ["block", "text-sm", "font-medium", "leading-6", "text-gray-900"]
        # Bard wrote the following code
        # email_field = self.fields["email"]
        # email_field.label.attrs["class"] = "block text-sm font-medium leading-6 text-gray-900"
        # self.fields["email"].widget.attrs[""]

class LogInForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
