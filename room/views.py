from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse
from .forms import RoomCreateForm
from .models import RoomBooking, Room
from django.shortcuts import get_object_or_404
from django.utils import timezone
from datetime import datetime
from datetime import datetime, timedelta, time

class HomeView(ListView):
    context_object_name = 'room_bookings'
    template_name = 'home.html'
    queryset = RoomBooking.objects.all()

    def get_context_data(self, **kwargs):
        self.object = None
        context = super(HomeView, self).get_context_data(**kwargs)
        context['rooms'] = Room.objects.all()
        return context

# class RoomCreateView(CreateView):
#     model = RoomBooking
#     form_class = RoomCreateForm
#     template_name = 'home.html'
#     # fields = ['title', 'start_time', 'end_time', 'room_id']

@api_view(['POST'])
def create(request):
    form = RoomCreateForm(request.POST)
    if form.is_valid():
        roombooking = form.save(commit=False)
        roombooking.title = request.data['title']
        roombooking.start_time = request.data['start_time']
        roombooking.end_time = request.data['end_time']
        roombooking.room_id = request.data['room_id']
        roombooking.save()

    return Response('')

