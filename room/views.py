from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
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
    roombooking_list = RoomBooking.objects.all()
    form = RoomCreateForm(request.POST)

    if roombooking_list.count() == 0:
        if form.is_valid():
            roombooking = form.save(commit=False)
            # roombooking.title = request.data['title']
            # roombooking.start_time = request.data['start_time']
            # roombooking.end_time = request.data['end_time']
            # roombooking.room_id = request.data['room_id']
            roombooking.save()
            return redirect('/')

    start_day = datetime.strptime(request.data['start_time'], '%Y-%m-%d %H:%M').date()
    start_time = datetime.strptime(request.data['start_time'], '%Y-%m-%d %H:%M').time()
    end_time = datetime.strptime(request.data['end_time'], '%Y-%m-%d %H:%M').time()
    for roombooking in roombooking_list:
        if start_day == roombooking.start_time.date() and request.data['room_id'] == roombooking.room_id:
            if roombooking.end_time.time() > start_time and start_time >= roombooking.start_time.time():
                print('fail')
                return redirect('/')
            elif end_time > roombooking.start_time.time() and roombooking.start_time.time() >= start_time:
                print('fail')
                return redirect('/')
            else :
                print('success')
                if form.is_valid():
                    roombooking = form.save(commit=False)
                    # roombooking.title = request.data['title']
                    # roombooking.start_time = request.data['start_time']
                    # roombooking.end_time = request.data['end_time']
                    # roombooking.room_id = request.data['room_id']
                    roombooking.save()
                    return HttpResponseRedirect('http://127.0.0.1:8000/admin')

    return HttpResponseRedirect('http://127.0.0.1:8000/admin')