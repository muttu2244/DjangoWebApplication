
from django.shortcuts import render
from django.http import HttpResponse
from . models import Destination
# Create your views here.

def index(request):
    #return HttpResponse("Hello World")

    """
    dest1 = Destination()           #create a object of the class Destination defined in models
    dest1.name = "Mumbai"
    dest1.img =  "destination_1.jpg"
    dest1.price = 700
    dest1.desc = "city never sleeps"
    dest1.offer = False

    dest2 = Destination()
    dest2.name = "Hyderabad"
    dest2.img = "destination_2.jpg"
    dest2.price = 650
    dest2.desc = "Biryani -- Yummy Tasty"
    dest2.offer = True

    dest3 = Destination()
    dest3.name = "Bangalore"
    dest3.img = "destination_3.jpg"
    dest3.price = 650
    dest3.desc = "Garden City, IT Capital of India"
    dest3.offer = False

    dests = [dest1, dest2, dest3]
    """

    dests = Destination.objects.all()
    #return render(request,'index.html')         #render is used instead of HttpRequest
    return render(request, 'index.html', {'dests': dests})


