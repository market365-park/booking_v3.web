from django.views.generic import ListView, CreateView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .forms import RoomCreateForm
from .models import RoomBooking, Room


class AjaxableResponseMixin:
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super().form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            return JsonResponse(data)
        else:
            return response

class HomeView(ListView):
    context_object_name = 'room_bookings'
    template_name = 'home.html'
    queryset = RoomBooking.objects.all()

    def get_context_data(self, **kwargs):
        self.object = None
        context = super(HomeView, self).get_context_data(**kwargs)
        context['rooms'] = Room.objects.all()
        return context

class RoomCreateView(AjaxableResponseMixin, CreateView):
    model = RoomBooking
    form_class = RoomCreateForm
    template_name = 'home.html'


@api_view(['POST'])
def create(request):
    if request.method == 'POST':
        print(request)
    return Response('')

