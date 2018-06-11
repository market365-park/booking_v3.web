from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import RegisterForm, MyPasswordChangeForm, ProfileUpdateForm 
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from django.views.generic import UpdateView
from .models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class CreateUserView(CreateView):
    template_name = 'registration/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        c = {'form': form, }
        user = form.save(commit=False)
        # Cleaned(normalized) data
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        repeat_password = form.cleaned_data['password2']
        email = form.cleaned_data['email']
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        phone = form.cleaned_data['phone']

        if password != repeat_password:
            messages.error(self.request, "Passwords do not Match", extra_tags='alert alert-danger')
            return render(self.request, self.template_name, c)
        user.set_password(password)
        user.save()

        return super(CreateUserView, self).form_valid(form)


def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {'form': form})


@login_required
def change_password(request):
    if request.method == 'POST':
        form = MyPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = MyPasswordChangeForm(request.user)
    return render(request, 'registration/password_change_form.html', {
        'form': form
    })


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    # model = User
    # queryset = User
    form_class = ProfileUpdateForm
#    form_class = RegisterForm
    template_name = 'registration/profile_update.html'
    success_url = '/'

    def get_queryset(self):
        users = User.objects.all()
        return users
