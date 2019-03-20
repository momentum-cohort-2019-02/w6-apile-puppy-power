from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100, help_text="Enter username")

    def validate_username(self):
        data = self.username