from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from shakes.models import attendance, event, meetup
from .models import profile, resume, flyer
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, ResumeUpdateForm, FlyerUpdateForm, CompanyCreateForm

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}.')
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form })

@login_required
def get_profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        r_form = ResumeUpdateForm(request.POST, request.FILES)
        f_form = FlyerUpdateForm(request.POST, request.FILES)
        c_form = CompanyCreateForm(request.POST, request.FILES)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Account updated.')
            return redirect('profile')
        if f_form.is_valid():
            temp = f_form.save(commit=False)
            temp.name = request.user
            temp.save()
            messages.success(request, f'Flyer updated')
            return redirect('profile')
        if r_form.is_valid():
            temp = r_form.save(commit=False)
            temp.name = request.user
            temp.save()
            request.user.profile.resume = temp
            request.user.profile.save()
            messages.success(request, f'Resume updated')
            return redirect('profile')
        if c_form.is_valid():
            temp = c_form.save(commit=False)
            temp.admin = request.user
            temp.save()
            request.user.profile.company = temp
            request.user.profile.save()
            messages.success(request, f'Company Registered')
            return redirect('profile')
        if p_form.is_valid():
            p_form.save()
            messages.success(request, f'Public Info updated.')
            return redirect('profile')
        return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        r_form = ResumeUpdateForm()
        f_form = FlyerUpdateForm()
        c_form = CompanyCreateForm()

    context = {
        "resume": "",
        "files":"",
    }
    context["resume"] = request.user.profile.resume
    context["files"] = flyer.objects.filter(name=request.user).order_by('-time')
    return render(request, 'users/profile.html', context)

def other_profile(request, username):

    context = {
        "other_user": "",
        "docs": ""
    }
    other_user = get_object_or_404(User, username=username)
    context["other_user"] = profile.objects.filter(user = other_user).first()
    interactions = meetup.objects.filter(people=request.user and other_user)
    sharedDocs = []
    for interaction in interactions:
        event_name = interaction.eventObj
        shared = attendance.objects.filter(person=other_user, event=event_name).first()
        if(shared in sharedDocs):
            continue
        sharedDocs.append(shared)
    context["docs"] = sharedDocs
    return render(request, 'users/user_profile.html',context)

@login_required
def get_private(request):
    u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form,
    }
    return render(request, 'users/personal_form.html',context)

@login_required
def get_resume(request):
    r_form = ResumeUpdateForm()

    context = {
        'r_form': r_form,
    }
    return render(request, 'users/resume_form.html',context)

@login_required
def get_flyer(request):
    f_form = FlyerUpdateForm()

    context = {
        'f_form': f_form,
    }
    return render(request, 'users/flyer_form.html',context)

@login_required
def get_public(request):
    p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'p_form': p_form,
    }
    return render(request, 'users/public_form.html',context)

def show_resume(request):
    user_resume = request.user.profile.resume
    context = {
        "resume":user_resume
    }
    return render(request, 'users/resume.html',context)

def show_flyer(request):
    user_flyer = request.user.profile.flyer
    context = {
        "flyer":user_flyer
    }
    return render(request, 'users/flyer.html',context)

@login_required
def register_company(request):
    c_form = CompanyCreateForm()
    print("test")

    context = {
        'c_form': c_form,
    }
    return render(request, 'users/company_form.html', context)