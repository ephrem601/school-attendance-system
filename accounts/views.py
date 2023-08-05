from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from accounts.forms import UserProfileRegistrationForm, LoginForm
from django.contrib.auth.models import Group 
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .models import UserProfile
from django.contrib import messages
from django.contrib.auth import logout
 
def registration_view(request):
    if request.method == 'POST':
        form = UserProfileRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user_profile = form.save()
            user = user_profile.user
            group_name = user_profile.user_type.lower() + 's'
            try:
                group = Group.objects.get(name=group_name)
            except ObjectDoesNotExist:
                pass
            else:
                group.user_set.add(user)
            #return redirect('accounts:login')
            messages.success(request, 'Registration successful! You can now log in.')
            form = UserProfileRegistrationForm()
    else:
        #form = UserProfileRegistrationForm(user=request.user)
        form = UserProfileRegistrationForm()
    return render(request, 'accounts/registration.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                user_profile = UserProfile.objects.filter(user=user).first()
                if user_profile is not None:
                    print (user_profile.user_type)
                    login(request, user)
                    if user_profile.user_type == 'Principal':
                        return redirect('attendance:principal-attendance')
                    elif user_profile.user_type == 'Teacher':
                        return redirect('attendance:teacher-attendance')
                    else:
                        return redirect('attendance:student-attendance')
                else:
                    form.add_error(None, 'Invalid login credentials.')
            else:
                form.add_error(None, 'Invalid login credentials.')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


 

def logout_view(request):
    logout(request)
    return redirect('accounts:login')   # redirect to your desired page after logout