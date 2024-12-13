from django.shortcuts import render
from django.views import generic

def about(request):
    return render(request, 'about/about.html')  