from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.

from .models import FillUp
from .levels.opening_level import OpeningLevel

def index(request):
    level = OpeningLevel()
    name = User.objects.first().username
    context = {
        'name' : name,
        'tt' : level.enter(),
        'birthday': '12/6/1979',
        'numbers' : [1,2,3]
    }

    return render(request, 'mileage/index.html', context)

def other(request):
    context = {}
    return render(request, 'mileage/other.html', context)

def poop(request):
    what_i_typed = request.POST['charlieTheChooChoo']
    return HttpResponse("You entered <hr>%s<hr> into the box" % what_i_typed)

def new_fillup(request):
    context = {}
    return render(request, 'mileage/form.html', context)

def save_fillup(request):
    fillup = FillUp()
    fillup.odometer = request.POST['odometer']
    fillup.gallons = request.POST['gallons']
    fillup.cpg = request.POST['cpg']
    fillup.fuel_type = request.POST['fueltype']
    fillup.save()

    return redirect("/mileage/fillup")

def list_fillup(request):
    items = FillUp.objects.all()
    context = {
        'items' : items
    }
    return render(request, 'mileage/fillup_table.html', context)
