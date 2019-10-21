from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils import timezone

class company(models.Model):
    name = models.CharField(max_length=50)
    website = models.CharField(max_length=50)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    passcode = models.CharField(max_length=10)
    image = models.ImageField(default="profile_pics\default.jpg", upload_to="company_pics")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

class resume(models.Model):
    name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    resume_file = models.FileField(upload_to="resumes", null=True)
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.resume_file.url

class flyer(models.Model):
    company = models.ForeignKey(company, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    file = models.FileField(upload_to="flyers", null=True)
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.file.url


class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    job = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(default="profile_pics\default.jpg",upload_to="profile_pics")
    company = models.ForeignKey(company, on_delete=models.SET_NULL, null=True, blank=True)
    resume = models.OneToOneField(resume, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

