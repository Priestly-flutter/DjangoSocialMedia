from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_view(request, *args, **kwargs): # look up this code
    print(request.user)
    #return HttpResponse("<h1> Hello Priestly </h1>") # a string of HTML code
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs): # look up this code
    #return HttpResponse("<h1> Contact </h1>") # a string of HTML code
    return render(request, "contact.html", {})


def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about us",
        "my_number": 1842736,
        "my_list": [123,145,676]
    }
    return render(request, "about.html", my_context)