from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect


def return_room_view(request):
    return HttpResponseRedirect("/room")