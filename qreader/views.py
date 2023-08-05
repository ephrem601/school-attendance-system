from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from attendance.models import Attendance
from accounts.models import UserProfile 
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from datetime import datetime

@login_required
def qr_data(request):
    context = {
        'qr_data': None,
        'firstname': None,
        'fathername': None,
        'username': None,
        'profile_image':None,
        'qr_code': None,
        'timestamp': None,
        'reg_date': None,
        'user_type': None,
    }

    if request.method == 'POST':
        qr_data = request.POST.get('qr_data')
        context['qr_data'] = qr_data 
        if qr_data:
            userProfile = get_object_or_404(UserProfile, phone=qr_data)
            context['qr_data'] = qr_data
            context['firstname'] = userProfile.firstname
            context['fathername'] = userProfile.fathername
            context['username'] = userProfile.user.username
            context['phone'] = userProfile.phone
            context['profile_image'] = userProfile.profile_image.url
            context['timestamp'] = userProfile.timestamp
            context['qr_code'] =userProfile.qr_code.url
            context['user_type'] =userProfile.user_type
            datetime_obj = context['timestamp'].utcnow()   # Get the current datetime object
            context['timestamp'] =  datetime_obj.strftime('%Y-%m-%d %H:%M:%S')       # Extract the date component
            context['reg_date'] =  datetime_obj.strftime('%Y-%m-%d %H:%M:%S')  # Extract the time component eliminate the microsecond
           
            username = request.user.username
              
            if not Attendance.objects.filter(qr_code=qr_data).exists():
                registered_by = UserProfile.objects.get(user__username=username)
                attendance = Attendance(qr_code=qr_data, attended_user=userProfile, attended_date=context['reg_date'])
                attendance.save()  # save the instance before setting the many-to-many relationship
                attendance.registered_by.set([registered_by])
              
    if request.is_ajax():
        # if the request was made via AJAX, return the context data in JSON format
        return JsonResponse(context)
    else:
        # otherwise, render the QR reader template with the context data
        return render(request, 'qreader/qr.html', context)             
       

 