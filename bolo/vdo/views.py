from django.shortcuts import render

# Create your views here.
def vdo_home(request):
    return render(request,'vdo/index.html')

def room(request):
    return render(request,'vdo/room.html')