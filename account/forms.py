from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.contrib.auth import authenticate

class UserRegistrationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ('email','password1','password2')

# class RegisterForm(forms.Form):
#     email = forms.EmailField()
#     password = forms.CharField(widget=forms.PasswordInput)
#     password2 = forms.CharField(widget=forms.PasswordInput)

#     def clean_email(self):
#         email = self.cleaned_data["email"]

#         if User.objects.filter(email=email).exists():
#             raise forms.ValidationError("این ایمیل قبلاً ثبت شده است.")

#         return email

#     def clean(self):
#         cleaned_data = super().clean()

#         password = cleaned_data.get("password")
#         password2 = cleaned_data.get("password2")

#         if password and password2 and password != password2:
#             raise forms.ValidationError("رمزهای عبور یکسان نیستند.")

#         return cleaned_data

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        if email and password:
            user = authenticate(
                username=email,
                password=password
            )

            if user is None:
                raise forms.ValidationError(
                    "ایمیل یا رمز عبور اشتباه است."
                )

            cleaned_data["user"] = user

        return cleaned_data