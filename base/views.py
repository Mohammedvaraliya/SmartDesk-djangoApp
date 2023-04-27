from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def rooms(request):
    return render(request, 'room.html')