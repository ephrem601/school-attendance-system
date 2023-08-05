from django.db import models
from django.contrib.auth.models import User
import qrcode                      # additional imports
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
from django.utils import timezone

class UserProfile(models.Model):
    USER_TYPE_CHOICES = (
         ('', 'Select an option'),
        ('Principal', 'Principal'),
        ('Teacher', 'Teacher'),
        ('Student', 'Student'),
    )
    GRADE = (
        ('', 'Select an option'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
    )
    HOME_ROOM = (
        ('', 'Select an option'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=255)
    fathername = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=255)
    profile_image = models.ImageField(upload_to='profiles/')
    timestamp = models.DateTimeField(default=timezone.now)
    user_type = models.CharField(max_length=50, choices=USER_TYPE_CHOICES)
    grade = models.CharField(max_length=50, choices=GRADE, null=True, blank=True)
    home_room = models.CharField(max_length=50, choices=HOME_ROOM, null=True, blank=True)
    qr_code = models.ImageField(upload_to='QRCodes/', blank=True)

    def __str__(self):
        return self.user.username
    
    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.phone)
        canvas= Image.new('RGB',(290, 290), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f'phone-{self.phone}'+'.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        buffer.close()
        canvas.close()
        super().save(*args, **kwargs)
    

 


