from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, FormView
from django.contrib.auth.models import User
from .models import meetup, event, attendance, band
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse
from .forms import createEventForm, joinEventForm, connectBandForm
from users.forms import FlyerUpdateForm
from django.contrib import messages
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from datetime import time
from .mixins import *
# Create your views here.

def home(request):
    context = {
        'shakes': meetup.objects.all(),
    }
    return render(request, 'shakes/home.html',context)

class ShakeListView(LoginRequiredMixin, ListView):
    model = meetup
    template_name = 'shakes/home.html'
    context_object_name = 'shakes'
   # paginate_by = 10

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)
        context['shakes'] = meetup.objects.filter(people=user).order_by('-date')
        return context

class EventListView(LoginRequiredMixin, ListView):
    model = meetup
    template_name = 'shakes/eventList.html'
    context_object_name = 'shakes'

    def get_context_data(self, **kwargs):
        user = self.request.user
        eventObj = event.objects.get(name = self.kwargs.get('eventObj'))
        context = super().get_context_data(**kwargs)
        context['shakes'] = meetup.objects.filter(people=user, eventObj = eventObj).order_by('-date')
        context['event'] = eventObj
        return context


class ShakeDetailView(DetailView):
    model = meetup
    template_name = 'shakes/shakes_detail.html'
    context_object_name = 'shake'

class ShakeCreateView(LoginRequiredMixin, CreateView):
    model = meetup
    template_name = 'shakes/shakes_create.html'
    context_object_name = 'shake'
    fields = ['people','eventObj']

class ShakeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = meetup
    success_url = "/"
    template_name = 'shakes/shakes_delete.html'
    context_object_name = 'shake'

    def test_func(self):
        meetup = self.get_object()
        return True

@login_required
def network(request):
    user = request.user
    shake_list = []
    context = {
        'shakes': shake_list,
    }
    for shake in meetup.objects.filter(people=user).order_by('-date'):
        interaction = {}
        interaction["personALink"] = shake.people.first().profile.image.url
        interaction["personA"] = shake.people.first().username
        interaction["personBLink"] = shake.people.last().profile.image.url
        interaction["personB"] = shake.people.last().username
        shake_list.append(interaction)

    return render(request, 'shakes/network.html',context)

@login_required
def connect(request):
    if request.method == "POST":
        b_form = connectBandForm(request.POST, request.FILES)
        if b_form.is_valid():
            bands = band.objects.filter(pk=int(b_form.cleaned_data.get('bandID')),
                                        Passcode=b_form.cleaned_data.get('password'))
            if bands.count() == 0:
                messages.error(request, f'Failed Authentication, Check Band Credentials')
                return redirect('home-connect')
            else:
                updateBand = bands.first()
                updateBand.LastUser = request.user
                updateBand.save()
                return redirect('events-join', b_form.cleaned_data.get('bandID'))

    context = {
        'b_form': connectBandForm
    }
    return render(request, 'shakes/connect.html', context)

class EventsView(LoginRequiredMixin, ListView):
    model = attendance
    template_name = 'shakes/events.html'
    context_object_name = 'events'

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)
        context['events'] = attendance.objects.filter(person=user).order_by('-date')
        return context

class EventCreateView(LoginRequiredMixin, FormView):
    form_class = createEventForm
    template_name = 'shakes/event_create.html'
    context_object_name = 'event'

    def get_success_url(self):
        return reverse('events')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

def messenger(request):
    return render(request, 'shakes/messenger.html')


@login_required
def EventJoinView(request, bandID):
    if not bandAuth(request.user, bandID):
        messages.success(request, "This band has not been authenticated yet")
        return redirect('home-connect')

    if request.method == "POST":
        e_form = joinEventForm(request.POST, request.FILES)
        f_form = FlyerUpdateForm(request.POST, request.FILES)
        print(f_form)
        if f_form.is_valid():

            temp = e_form.save(commit=False)
            temp.person = request.user
            bandUser = band.objects.filter(pk=bandID).first()
            temp.band = bandUser


            flyerf = f_form.save(commit=False)
            flyerf.name = request.user
            flyerf.save()

            temp.fileShared = flyerf
            temp.save()

            return redirect('live-path', bandID, temp.event)
    else:
        e_form = joinEventForm()
        f_form = FlyerUpdateForm()

    context = {
        "e_form": e_form,
        "f_form": f_form
    }
    return render(request, 'shakes/event_join.html', context)


# TODO Remove CSRF_Exempt make more secure
@csrf_exempt
def CreateShakeView(request):
    if request.method == "POST":
        band_id = request.POST.get('message')
        event_name = request.POST.get('event')
        other_user = attendance.objects.filter(band=band_id).order_by("-date").first()
        event_obj = event.objects.filter(name=event_name).first()
        shake = meetup.objects.create(eventObj=event_obj)
        shake.people.add(other_user.person)
        shake.people.add(request.user)
        shake.save()
    if request.method == "GET":
        new_shake = meetup.objects.filter(people=request.user).order_by("-date").first()
        data = str(new_shake.id) + ',' + str(new_shake.eventObj) + ',' + str(new_shake.people.first().username) + \
                ',' + str(new_shake.people.first().profile.image.url) + ',' + str(new_shake.people.last().username) + \
                ',' + str(new_shake.people.last().profile.image.url) + ',' + new_shake.date.strftime('%b/%d/%Y')

        return HttpResponse(data)

    return HttpResponse('')

class ShakeListViewLive(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = meetup
    template_name = 'shakes/live-home.html'
    context_object_name = 'shakes'
   # paginate_by = 10

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)
        context['shakes'] = meetup.objects.filter(people=user).order_by('-date')
        context['event'] = self.kwargs['eventObj']
        context['band'] = self.kwargs['bandID']
        return context

    def test_func(self):
        user = self.request.user
        eventname = self.kwargs['eventObj']
        bandID = int(self.kwargs['bandID'])
        bandObj = band.objects.filter(pk=bandID).first()
        eventObj = event.objects.filter(name=eventname).first()
        attendaceObj = attendance.objects.filter(person=user,band=bandObj, event=eventObj)
        if attendaceObj.count() == 0:
            return False
        return True

    def handle_no_permission(self):
        messages.success(self.request, "This band has not been authenticated yet")
        return redirect('home-connect')
