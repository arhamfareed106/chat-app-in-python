from django.shortcuts import render, redirect
from .models import Room, Message # type: ignore

def CreateRoom(request):  
    if request.method == 'POST':
        username = request.POST.get('username') 
        room = request.POST.get('room')
        
        try:
            get_room = Room.objects.get(room_name=room)
            return redirect('room', room_name=get_room.room_name, username=username)
        except Room.DoesNotExist:
            new_room = Room(room_name=room)
            new_room.save()
            return redirect('room', room_name=room, username=username)

    return render(request, 'index.html')

def MessageView(request, room_name, username):
    get_room= Room.objects.get(room_name=room_name)
    get_message = Message.objects.filter(room=get_room)
    context = {
        'room_name': room_name,
        'user': username,
        'messages': get_message
    }
    return render(request, '_message.html', context)
