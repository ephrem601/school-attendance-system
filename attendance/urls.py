 
from django.urls import path
from attendance.views import(
    PrincipalListView,
    TeacherListView,
    StudentListView,
    PrincipalAttendanceListView,
    TeacherAttendanceListView,
    StudentAttendanceListView,
    AttendanceListView,
    PrincipalUpdateView,
    TeacherUpdateView,
    StudentUpdateView,
    PrincipalDeleteView,
    TeacherDeleteView,
    StudentDeleteView,
    chart,
    
)


app_name = 'attendance'

urlpatterns = [
    path('principal/', PrincipalListView.as_view(), name='principal'),
    path('teacher/', TeacherListView.as_view(), name='teacher'),
    path('student/', StudentListView.as_view(), name='student'),

    path('principal-attendance/', PrincipalAttendanceListView.as_view(), name='principal-attendance'),
    path('teacher-attendance/', TeacherAttendanceListView.as_view(), name='teacher-attendance'),
    path('student-attendance/', StudentAttendanceListView.as_view(), name='student-attendance'),
    
    path('dashboard/', AttendanceListView.as_view(), name='dashboard'),

    path('principal/edit/<int:pk>/', PrincipalUpdateView.as_view(), name='principal-edit'),
    path('teacher/edit/<int:pk>/', TeacherUpdateView.as_view(), name='teacher-edit'),
    path('student/edit/<int:pk>/', StudentUpdateView.as_view(), name='student-edit'),

    path('principal/delete/<int:pk>/', PrincipalDeleteView.as_view(), name='profile-delete'),
    path('teacher/delete/<int:pk>/', TeacherDeleteView.as_view(), name='profile-delete'),
    path('student/delete/<int:pk>/', StudentDeleteView.as_view(), name='profile-delete'),
    
    path('chart/', chart, name='chart'),
]