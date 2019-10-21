from .models import band
from django.core.exceptions import PermissionDenied

def bandAuth(user, bandID):
    bandObj = band.objects.filter(pk=bandID)
    if bandObj.count() == 0:
        return False
    if bandObj.first().LastUser != user:
        return False
    return True
