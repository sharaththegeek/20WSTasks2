from django import forms
from board.models import User
from board.models import UserProfile

class LoginForm(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput())

    def clean_email(self):
        email=self.cleaned_data.get('email')
        UObj=User.objects.get(email=email)
        if not UObj:
            raise forms.ValidationError("Incorrect Email")
        else:
            return email
    
    def clean_password(self):
        password=self.cleaned_data.get('password')
        email=self.cleaned_data.get('email')
        UObj=User.objects.get(email=email)
        if not UObj:
            raise forms.ValidationError("Incorrect Email")
        else:
            passwd=UObj.password
            if password==passwd:
               return password
            else:
               raise forms.ValidationError("Incorrect Password")

class UserDetails(forms.Form):
    firstName=forms.CharField(max_length=20)
    lastName=forms.CharField(max_length=20)
    email=forms.EmailField()
    password=forms.CharField(max_length=20)
    sex=forms.CharField(max_length=10)
    
    def clean_email(self):
        email=self.cleaned_data.get('email')
        UObj=User.objects.filter(email=email)
        if UObj:
            raise forms.ValidationError("Email already exists")
        else:
            return email

