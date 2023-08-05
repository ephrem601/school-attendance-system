from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from accounts.models import UserProfile


class UserProfileRegistrationForm(forms.ModelForm):
     
    username = forms.CharField(max_length=255)
    firstname = forms.CharField(max_length=255)
    fathername = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=255)
    phone = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    profile_image = forms.ImageField()
    user_type = forms.ChoiceField(choices=UserProfile.USER_TYPE_CHOICES)
    grade = forms.ChoiceField(choices=UserProfile.GRADE, required=False)
    home_room = forms.ChoiceField(choices=UserProfile.GRADE, required=False)
    #user = forms.ModelChoiceField(queryset=User.objects.none(), widget=forms.HiddenInput())
    class Meta:
        model = UserProfile
        fields = ['username', 'firstname', 'fathername', 'email', 'phone', 'password', 'confirm_password', 'profile_image', 'user_type','grade', 'home_room']
    
    #def __init__(self, user, *args, **kwargs):
    def __init__(self, *args, **kwargs):
        #self.user = user
        super().__init__(*args, **kwargs)
        #self.fields['user_type'].initial = UserProfile.objects.get(user=user).user_type
        #if not self.fields['user_type'].initial == 'Student':
            #self.fields['grade'].widget = forms.HiddenInput()
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Register'))

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        username = cleaned_data.get('username')
        phone = cleaned_data.get('phone')

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username is already taken.")
        
        if UserProfile.objects.filter(phone=phone).exists():
            raise forms.ValidationError("Phone Number is already taken.")

        return cleaned_data

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password']
        )
        
        user_type = self.cleaned_data['user_type']
        grade = self.cleaned_data['grade']
        home_room = self.cleaned_data['home_room']
        user_profile = UserProfile(
            firstname=self.cleaned_data['firstname'],
            fathername=self.cleaned_data['fathername'],
            email=self.cleaned_data['email'],
            phone=self.cleaned_data['phone'],
            profile_image=self.cleaned_data['profile_image'],
            user=user,
            user_type=user_type,
            grade = grade,
            home_room=home_room,
        )
        if commit:
            user_profile.save()
        return user_profile    

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)