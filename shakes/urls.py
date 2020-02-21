from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', ShakeListView.as_view(), name = "home-path"),
    path('live/<int:bandID>/<str:eventObj>/', ShakeListViewLive.as_view(), name = "live-path"),
    path('shake/<int:pk>/', ShakeDetailView.as_view(), name = "post-detail"),
    path('shake/new/', ShakeCreateView.as_view(), name = "post-create"),
    path('shake/MLShake/', views.ai, name = "post-ai"),
    path('shake/<int:pk>/delete/', ShakeDeleteView.as_view(), name = "post-delete"),
    path('connect/', views.connect, name = "home-connect"),
    path('network/', views.network, name="network"),
    path('events/', EventsView.as_view(), name="events"),
    path('events/create/', EventCreateView.as_view() , name="events-create"),
    path('events/join/<int:bandID>/', EventJoinView , name="events-join"),
    path('makeshake/', views.CreateShakeView , name="make-shake"),
    path('getPrediction/', views.recievePrediction , name="recieve-pred"),
    path('events/<str:eventObj>/', EventListView.as_view(), name="event-list"),
    path('messenger/', views.messenger, name="messenger"),
]
