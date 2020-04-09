from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=100)
    photo = models.CharField(max_length=100)
    last_logout = models.DateTimeField(null=True, blank=True)
    login_count = models.IntegerField(null=True, blank=True)


