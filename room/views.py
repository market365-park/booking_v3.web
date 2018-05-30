from django.shortcuts import redirect, render, render_to_response
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
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(LoginRequiredMixin, ListView):
    context_object_name = 'room_bookings'
    template_name = 'room_home.html'
    queryset = RoomBooking.objects.all()

    def get_context_data(self, **kwargs):
        self.object = None
        context = super(HomeView, self).get_context_data(**kwargs)
        context['rooms'] = Room.objects.all()
        return context

# class RoomCreateView(CreateView):
#     model = RoomBooking
#     form_class = RoomCreateForm
#     template_name = 'room_home.html'
#     # fields = ['title', 'start_time', 'end_time', 'room_id']

@api_view(['GET','POST'])
def booking(request):
    if request.method == 'POST':
        roombooking_list = RoomBooking.objects.all()
        form = RoomCreateForm(request.POST)
        start_day = datetime.strptime(request.data['start_time'], '%Y-%m-%d %H:%M').date()
        start_time = datetime.strptime(request.data['start_time'], '%Y-%m-%d %H:%M').time()
        end_time = datetime.strptime(request.data['end_time'], '%Y-%m-%d %H:%M').time()
        url = "/room/?start=" + str(start_day)

        if roombooking_list.count() == 0:
            if form.is_valid():
                roombooking = form.save(commit=False)
                roombooking.owner = request.user
                roombooking.save()
                return redirect(url)

        for roombooking in roombooking_list:
            if start_day == roombooking.start_time.date() and request.data['room_id'] == roombooking.room_id:
                if roombooking.end_time.time() > start_time and start_time >= roombooking.start_time.time():
                    return render_to_response('message.html', {'message': '이미 예약된 시간입니다.', 'start_day': url})

                elif end_time > roombooking.start_time.time() and roombooking.start_time.time() >= start_time:
                    return render_to_response('message.html', {'message': '이미 예약된 시간입니다.', 'start_day': url})

                else :
                    pass

        if form.is_valid():
            roombooking = form.save(commit=False)
            roombooking.owner = request.user
            roombooking.save()
            return redirect(url)

    elif request.method == 'GET':
        delete_event_id = request.GET['delete_event_id']
        delete_event_object = RoomBooking.objects.get(id=delete_event_id)
        start_day = delete_event_object.start_time.date()
        url = "/room/?start=" + str(start_day)

        if delete_event_object.owner == request.user:
            delete_event_object.delete()

            return redirect(url)

        else:
            return render_to_response('message.html', {'message': '자신의 예약만 삭제할 수 있습니다.', 'start_day': url})

