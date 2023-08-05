from django.urls import path
from .views import registration_view, login_view, logout_view

app_name = 'accounts'


urlpatterns = [
    path('registration/', registration_view, name='registration'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]