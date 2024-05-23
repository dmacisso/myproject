# from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    # return HttpResponse("Hello, world. You're at the myproject home page.")
    return render(request, 'home.html')


def about(request):
    # return HttpResponse("Hello, world. You're at the myproject about page.")
    return render(request, 'about.html')
    
