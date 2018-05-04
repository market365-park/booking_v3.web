from django.views.generic import ListView, CreateView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .forms import CreateForm
from .models import RoomBooking, Room


class HomeView(ListView, CreateView):
    model = RoomBooking
    form_class = CreateForm
    context_object_name = 'room_bookings'
    template_name = 'home.html'
    queryset = RoomBooking.objects.all()

    def get_context_data(self, **kwargs):
        self.object = None
        context = super(HomeView, self).get_context_data(**kwargs)
        context['rooms'] = Room.objects.all()
        return context


@api_view(['POST'])
def create(request):
    if request.method == 'POST':
        print(request)
    return Response('')

