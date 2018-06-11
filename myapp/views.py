from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required

@login_required
def return_room_view(request):
    return HttpResponseRedirect("/room")

class GateView(TemplateView):
	template_name = 'gate.html'
