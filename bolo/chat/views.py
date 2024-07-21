from django.shortcuts import render,redirect
from .models import Room,Message
from django.http import HttpResponse,JsonResponse

# Create your views here.
def chat_home(request):
    return render(request,'chat/index.html')
    
def chat_room(request,room):
    username=request.GET.get("username")
    room_details=Room.objects.get(name=room)
    return render(request,'chat/room.html',{
        'username':username,
        'room':room,
        'room_details':room_details
    })  

def checkroom(request):
    room=request.POST["room_name"]
    username=request.POST["user_name"]

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room= Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)

def send(request):
    message = request.POST['message']
    room_id = request.POST['room_id']
    username = request.POST['username']

    new_message= Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent')

def getMessages(request,room):
    room_details=Room.objects.get(name=room)
    # messages=Message.objects.raw("SELECT * FROM MESGE OSARDER BY 'Date' DESC;")
    messages=Message.objects.filter(room=room_details.id).order_by('-date')
    return JsonResponse({"messages":list(messages.values())})
    