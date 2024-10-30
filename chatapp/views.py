from django.shortcuts import render, redirect
from .models import Room  # type: ignore

def CreateRoom(request):  
    if request.method == 'POST':
        username = request.POST.get('username') 
        room = request.POST.get('room')
        
        # Check if the room exists; otherwise, create a new room
        try:
            get_room = Room.objects.get(room_name=room)
            return redirect('room', room_name=get_room.room_name, username=username)
        except Room.DoesNotExist:
            # Room doesn't exist, so create and save it
            new_room = Room(room_name=room)
            new_room.save()
            return redirect('room', room_name=new_room.room_name, username=username)

    # Render the default form for GET request
    return render(request, 'index.html')

def MessageView(request, room_name, username):
    # Pass room name and username to the chat view
    context = {
        'room_name': room_name,
        'username': username,
    }
    return render(request, '_message.html', context)
