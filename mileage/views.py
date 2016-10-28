from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    some_text = """
    Hello!
    
    This is a formatted
    
        text block
    """
    context = {'name' : "Chris", 'tt' : some_text}
    return render(request, 'mileage/index.html', context) 