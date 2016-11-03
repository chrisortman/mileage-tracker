from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    some_text = """
    Hello!
    
    This is a formatted
    
        text block
    """
    
    
    name = User.objects.first().username
    context = {
        'name' : name,
        'tt' : some_text,
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