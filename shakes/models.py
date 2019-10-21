from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from users.models import flyer


class band(models.Model):
    LastUser = models.ForeignKey(User, on_delete= models.SET_NULL, null=True, blank=True)
    Passcode = models.CharField(max_length=10)

    def __str__(self):
        return str(self.pk)

class event(models.Model):
    name = models.CharField(max_length=100)
    startTime = models.DateField()
    endTime = models.DateField()
    location = models.CharField(max_length=100)
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class meetup(models.Model):
   people = models.ManyToManyField(User)
   id = models.AutoField(primary_key=True)
   eventObj = models.ForeignKey(event, on_delete= models.CASCADE, default=0)
   date = models.DateTimeField(default=timezone.now)

   def get_absolute_url(self):
      return reverse('home-path')

   def __str__(self):
       return str(self.id) + "_" + self.eventObj.name

class attendance(models.Model):
    person = models.ForeignKey(User, on_delete= models.CASCADE, null=True)
    event = models.ForeignKey(event, on_delete= models.SET_NULL, null=True)
    band = models.ForeignKey(band, on_delete= models.SET_NULL, null=True)
    userType = models.CharField(max_length=4, default="0")
    date = models.DateTimeField(default=timezone.now)
    fileShared = models.ForeignKey(flyer, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.person.username + "_" + self.event.name)