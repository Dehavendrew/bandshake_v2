from django.contrib import admin
from .models import profile,resume, flyer, company

admin.site.register(profile)
admin.site.register(resume)
admin.site.register(flyer)
admin.site.register(company, name="Companies")
