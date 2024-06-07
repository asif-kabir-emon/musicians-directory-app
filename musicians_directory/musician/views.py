from django.shortcuts import render
from .models import Musician
from .forms import MusicianForm

def add_musician(request):
    if request.method == 'POST':
        form = MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            form = MusicianForm()
    else:
        form = MusicianForm()
    return render(request, "add_musician.html", {'form': form})