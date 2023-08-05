from django.views.generic import ListView
from accounts.models import UserProfile
from attendance.models import Attendance
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views.generic.edit import UpdateView, DeleteView
from attendance.forms import PrincipalForm, TeacherForm, StudentForm
from django.urls import reverse_lazy, reverse
from django.shortcuts import render
from django.contrib import messages


class PrincipalListView(LoginRequiredMixin, ListView):
    model = UserProfile
    template_name = 'attendance/principal_list.html'
    context_object_name = 'principal_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user_type='Principal')
        return queryset
    
    
class TeacherListView(LoginRequiredMixin, ListView):
    model = UserProfile
    template_name = 'attendance/teacher_list.html'
    context_object_name = 'teacher_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user_type='Teacher')
        return queryset
    

class StudentListView(LoginRequiredMixin, ListView):
    model = UserProfile
    template_name = 'attendance/student_list.html'
    context_object_name = 'student_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user_type='Student')
        return queryset
 

class PrincipalAttendanceListView(LoginRequiredMixin, ListView):
    model = Attendance
    template_name = 'attendance/attendance_principal_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # retrieve all UserProfile objects and their related Attendance objects
        user_profile_objects = UserProfile.objects.all()
        attendance_list = Attendance.objects.all()

        # add the UserProfile and Attendance objects to the context
        context['user_profile_objects'] = user_profile_objects
        context['attendance_list'] = attendance_list

        
        # otherwise, return the context dictionary
        return context


class TeacherAttendanceListView(LoginRequiredMixin, ListView):
    model = Attendance
    template_name = 'attendance/attendance_teacher_list.html'
     
    #user_profile_objects = UserProfile.objects.filter(phone__in=Attendance.objects.values_list('qr_code', flat=True)).prefetch_related('attendance_set')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # retrieve all UserProfile objects and their related Attendance objects
        attendance_list = Attendance.objects.all()
        context['attendance_list'] = attendance_list
        return context


class StudentAttendanceListView(LoginRequiredMixin, ListView):
    model = Attendance
    template_name = 'attendance/attendance_student_list.html'
    
    #user_profile_objects = UserProfile.objects.filter(phone__in=Attendance.objects.values_list('qr_code', flat=True)).prefetch_related('attendance_set')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # retrieve all UserProfile objects and their related Attendance objects
        user_profile_objects = UserProfile.objects.all()
        attendance_list = Attendance.objects.all()
        # add the UserProfile and Attendance objects to the context
        context['user_profile_objects'] = user_profile_objects
        context['attendance_list'] = attendance_list
        return context
    


class AttendanceListView(LoginRequiredMixin, ListView):
    model = Attendance
    template_name = 'attendance/attendance_list.html'
     
    #user_profile_objects = UserProfile.objects.filter(phone__in=Attendance.objects.values_list('qr_code', flat=True)).prefetch_related('attendance_set')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # retrieve all UserProfile objects and their related Attendance objects
        user_profile_objects = UserProfile.objects.all()
        attendance_list = Attendance.objects.all()
        # add the UserProfile and Attendance objects to the context
        context['user_profile_objects'] = user_profile_objects
        context['attendance_list'] = attendance_list
    
        return context


class PrincipalUpdateView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = PrincipalForm
    template_name = "attendance/principal_edit.html"
     
    def get_success_url(self):
        return reverse('attendance:principal')

class TeacherUpdateView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = TeacherForm
    template_name = "attendance/staff_edit.html"
     
    def get_success_url(self):
        return reverse('attendance:teacher')

class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = StudentForm
    template_name = "attendance/staff_edit.html"
     
    def get_success_url(self):
        return reverse('attendance:student')
 
 

class PrincipalDeleteView(LoginRequiredMixin, DeleteView):
    model = UserProfile
    template_name = 'attendance/confirm_principal_delete.html'
    success_url = reverse_lazy('attendance:principal')
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return render(request, self.template_name, context)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Model instance deleted successfully.')
        return super().delete(request, *args, **kwargs)
    
class TeacherDeleteView(LoginRequiredMixin, DeleteView):
    model = UserProfile
    template_name = 'attendance/confirm_teacher_delete.html'
    success_url = reverse_lazy('attendance:teacher')
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return render(request, self.template_name, context)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Model instance deleted successfully.')
        return super().delete(request, *args, **kwargs)
    

class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = UserProfile
    template_name = 'attendance/confirm_student_delete.html'
    success_url = reverse_lazy('attendance:student')
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return render(request, self.template_name, context)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Model instance deleted successfully.')
        return super().delete(request, *args, **kwargs)
    


def chart(request):
        #my_data = UserProfile.objects.exclude(firstname__isnull=True).count()
        num_of_principals = UserProfile.objects.filter(user_type='Principal').count()
        num_of_teachers = UserProfile.objects.filter(user_type='Teacher').count()
        num_of_students = UserProfile.objects.filter(user_type='Student').count()

        data = {
                'num_of_principals':num_of_principals,
                'num_of_teachers':num_of_teachers,
                'num_of_students':num_of_students
            } 

        return JsonResponse(data, safe=False)

