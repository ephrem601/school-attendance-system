from django.urls import path
from qreader.views import qr_data 
app_name = 'qreader'

urlpatterns = [ 
     
    path('qr-data/', qr_data, name='qr-data'),   
]