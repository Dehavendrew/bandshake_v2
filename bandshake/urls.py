"""bandshake URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name="users/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="users/logout.html"), name='logout'),
    path('profile/', user_views.get_profile, name='profile'),
    path('profile/private/', user_views.get_private, name='profile-private'),
    path('profile/get-resume/', user_views.get_resume, name='profile-resume'),
    path('profile/resume/', user_views.show_resume, name='doc-resume'),
    path('profile/get-flyer/', user_views.get_flyer, name='profile-flyer'),
    path('profile/flyer/', user_views.show_flyer, name='doc-flyer'),
    path('profile/get-public/', user_views.get_public, name='profile-public'),
    path('user/<str:username>/', user_views.other_profile, name='other-user'),
    path('company/register/', user_views.register_company, name='company-create'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name="users/password_reset.html"),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html"),
         name='password_reset_confirm'),
    path('password-reset-complete',
         auth_views.PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"),
         name='password_reset_complete'),
    path('', include('shakes.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)