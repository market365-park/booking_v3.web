from django.views.generic import ListView, CreateView

from .models import RoomBooking, Room
from .forms import CreateForm

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
