"""myapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import include, path
from django.contrib.auth import views as auth_views
from .forms import MyLoginForm, MyPasswordChangeForm
from .views import CreateUserView, signup

app_name = 'account'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
#    path('register/', CreateUserView.as_view(), name='register'),
    path('register/', signup, name='register'),
    path('signin/', auth_views.login,
        {'authentication_form': MyLoginForm,
         'template_name': 'registration/login.html',
         'redirect_field_name': 'home'}, name='signin'),
    # url(r'^account/password_change/$', auth_views.password_change,
		# {'post_change_redirect' :'/',
		#  'password_change_form': MyPasswordChangeForm }, name='password_change'),
    # url(r'^account/profile/(?P<pk>[0-9]+)/edit/$', ProfileUpdateView.as_view(), name='edit_profile'),
]
