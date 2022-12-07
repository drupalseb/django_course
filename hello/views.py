from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "hello/index.html") # template index.html is inside folder templates/hello. Folder "templates" could be use to multiple apps, that good practise is to put template in separate folder called as app name

#def index(request):
 #   return HttpResponse("Hello")

def brian(request):
    return HttpResponse("Hello Brian")    

def david(request):
    return HttpResponse("Hello David")    

#def greet(request, name):
 #       return HttpResponse(f"Hello, {name.capitalize()}!")
 # modify above function to render httpResponse to return some tamplate

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })