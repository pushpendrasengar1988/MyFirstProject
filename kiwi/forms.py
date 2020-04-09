from django import forms

from django.contrib.auth.models import User


class UserSignUpForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ('username','email','password')

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.exclude(username=self.instance.username).filter(username=username).exists():
            raise forms.ValidationError('Username "%s" is already in use.' % username)
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.exclude(username=self.instance.username).filter(email=email).exists():
            raise forms.ValidationError('Email "%s" is already in use.' % email)
        return email

    def clean_password(self):
        cleaned_data = super(UserSignUpForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("password-repeat")

        if password != confirm_password:
            raise forms.ValidationError(
                "Password and Repeat Password does not match."
            )
        return password

# class UserUpdateForm(forms.ModelForm):
#
#     class Meta():
#         model = User
#         fields = ('username','email')
#
#     def clean_username(self):
#
#         # username = self.cleaned_data['username']
#         # if User.objects.exclude(username=self.instance.username).filter(username=username).exists():
#         #     raise forms.ValidationError('Username "%s" is already in use.' % username)
#         return username
#
#     def clean_email(self):
#         email = self.cleaned_data['email']
#         if User.objects.exclude(username=self.instance.username).filter(email=email).exists():
#             raise forms.ValidationError('Email "%s" is already in use.' % email)
#         return email








