from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView

class TempView(TemplateView):
    template_name = 'aboutme_home.html'

