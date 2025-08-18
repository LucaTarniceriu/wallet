from django.shortcuts import render
from django.http import HttpResponse
from .forms import *

# Create your views here.

def login(request):
    context = {}
    context['form'] = UsernameForms()
    return render(request, "login.html", context)

def home(request):
    context = {}

    if request.method == "POST":
        request.session['username'] = request.POST.get('username')
        context['username'] = request.POST.get('username')

    return render(request, "home.html", context)