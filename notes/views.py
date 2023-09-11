from django.shortcuts import render
from .models import Note


# Create your views here.

def add_note(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            return render(request, 'notes/add_note.html', context={'user_id': request.user.id})
        print(request.user.id)
        new_note = Note(text=request.POST.get('note-text'), author=request.user.id)
        new_note.save()
        return render(request, 'reg/reg_other.html', context={'response': "Congrats! You've added your note!"})
    return render(request, './reg/reg_other.html', context={'response': "We're not properly introduced yet, please register or log in"})