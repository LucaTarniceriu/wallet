from django.shortcuts import render, redirect
from django.http import HttpResponse
from openpyxl.styles.builtins import total

from .forms import *
from .models import EntryModel, TotalValues

# Create your views here.

def login(request):
    context = dict()
    context['form'] = UsernameForms()
    return render(request, "login.html", context)

def home(request):
    context = dict()

    if request.method == "POST":
        request.session['username'] = request.POST.get('username')
        context['username'] = request.POST.get('username')

        if TotalValues.objects.filter(user=request.session['username']):
            context['total'] = TotalValues.objects.filter(user=request.session['username'])[0].total
            context['leftWith'] = TotalValues.objects.filter(user=request.session['username'])[0].thisMonth
        else:
            return redirect('login')

    else:
        return render(request, "error.html")

    return render(request, "home.html", context)

def viewTransactions(request):
    context = dict()
    if not request.session.get('username') or request.session.get('username') == ("empty"):
        return render(request, "error.html")
    else:
        context['transactions'] = EntryModel.objects.all()
        return render(request, "viewTransactions.html", context)

def addTransaction(request):
    pass

def logout(request):
    request.session['username'] = "empty"
    return redirect('login')