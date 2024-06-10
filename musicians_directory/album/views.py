from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Album
from .forms import AlbumForm

@login_required
def add_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            form = AlbumForm()
    else:
        form = AlbumForm()
    return render(request, "add_album.html", {'form': form})

@login_required
def delete_album(request, id):
    album = Album.objects.get(pk=id)
    album.delete()
    return redirect('home')

@login_required
def edit_album(request, id):
    album = Album.objects.get(pk=id)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AlbumForm(instance=album)
    return render(request, "edit_album.html", {'form': form})