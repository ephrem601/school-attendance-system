from django.db import models
from django.contrib.auth.models import User
from accounts.models import UserProfile
from django.utils import timezone
# Create your models here.
 

class Attendance(models.Model):
    qr_code = models.CharField(max_length=255)
    attended_user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='attendance')
    registered_by = models.ManyToManyField(UserProfile, related_name='registration')
    attended_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.attended_user.user.username