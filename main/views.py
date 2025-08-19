from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
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


    if request.method == "POST" or request.session.get('username'):
        if request.method == "POST":
            request.session['username'] = request.POST.get('username')
            request.session.modified = True
        print("user:", request.session.get('username'))
        context['username'] = request.session.get('username')

        if TotalValues.objects.filter(user=request.session.get('username')).exists():
            context['total'] = TotalValues.objects.filter(user=request.session.get('username'))[0].total
            context['leftWith'] = TotalValues.objects.filter(user=request.session.get('username'))[0].thisMonth
        else:
            print("user does not exist")
            return redirect('login')

    else:
        return render(request, "error.html")

    return render(request, "home.html", context)

def viewTransactions(request):
    context = dict()
    if not request.session.get('username') or request.session.get('username') == ("empty"):
        return render(request, "error.html")
    else:
        context['transactions'] = EntryModel.objects.filter(user=request.session.get('username'))
        return render(request, "viewTransactions.html", context)

def addTransaction(request):
    context = dict()
    context['addForm'] = AddForm()

    return render(request, "addTransaction.html", context)

def processTransaction(request):
    if request.method == "POST":

        user = request.session.get('username')
        value = request.POST.get('value')
        transactionDate = request.POST.get('transactionDate')
        source = request.POST.get('source')
        borrowed = request.POST.get('borrowed') or False
        toMonthly = request.POST.get('toMonthly') or False
        add10pcent = request.POST.get('add10pcent') or False

        entry = EntryModel(user=user, value=value, date=transactionDate, source=source, borrowed=borrowed)
        entry.save()

        userTotal = TotalValues.objects.get(user=request.session.get('username'))
        userTotal.total += int(value)
        print("added to total")
        if source != "salar":
            if toMonthly:
                userTotal.thisMonth += int(value)
                print("added to monthly")
            if add10pcent:
                userTotal.thisMonth += -1*(int(value)/10)
                userTotal.total += -1*(int(value)/10)
                entry = EntryModel(user=user, value=-1*(int(value)/10), source="10%", borrowed=False)
                entry.save()
        else:
            userTotal.thisMonth = int(value)
            print("added salar")
            entry = EntryModel(user=user, value=-1*(int(value)/10), source="10%", borrowed=False)
            userTotal.thisMonth += -1*(int(value)/10)
            userTotal.total += -1*(int(value)/10)
            print("added 10%")
            entry.save()

        userTotal.save()


        return redirect('home')
    else:
        return render(request, "error.html")

def logout(request):
    request.session['username'] = "empty"
    return redirect('login')