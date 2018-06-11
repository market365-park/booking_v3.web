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
from django.urls import include, path
from .views import *

app_name = 'aboutme'
urlpatterns = [
	path('<int:pk>', TempView.as_view(), name='home'),

#	path('signup/', signup, name='signup'),
#    path('signin/', auth_views.login,
#		{'authentication_form': MyLoginForm, 'template_name': 'registration/login.html', 'redirect_field_name': 'home'},
#		 name='signin'),
#
#    path('password/', change_password, name='change_password'),
#    path('profile/<int:pk>/edit/', ProfileUpdateView.as_view(), name='edit_profile'),
]
