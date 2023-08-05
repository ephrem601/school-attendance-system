from django import forms
from accounts.models import UserProfile

class PrincipalForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['user','firstname', 'fathername','email', 'phone', 'profile_image','user_type', 'qr_code']


class TeacherForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['user','firstname', 'fathername','email', 'phone', 'profile_image','user_type','qr_code','home_room']


class StudentForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['user','firstname', 'fathername','email', 'phone', 'profile_image', 'user_type','grade','qr_code']
