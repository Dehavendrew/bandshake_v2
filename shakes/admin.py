from django.contrib import admin
from .models import meetup, event, band, attendance

admin.site.register(meetup)
admin.site.register(event)
admin.site.register(band)
admin.site.register(attendance)
