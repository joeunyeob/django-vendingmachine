from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.base import TemplateView, View
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def index_redirect(request):
    return redirect('/VendingMachine/')


class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')


class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'
