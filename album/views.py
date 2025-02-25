from django.shortcuts import render, redirect
from .forms import AlbumForm
from .models import Album

# Create your views here.
def add_album(request):
    if request.method == 'POST':
        albumForm = AlbumForm(request.POST)
        if albumForm.is_valid():
            albumForm.save()
            return redirect('add_album')
    else:
        albumForm = AlbumForm()
    return render(request, 'add_album.html', {'albumForm': albumForm})

def edit_album(request, id):
    album = Album.objects.get(pk=id)
    albumForm = AlbumForm(instance=album)
    
    if request.method == 'POST':
        albumForm = AlbumForm(request.POST, instance=album)
        if albumForm.is_valid():
            albumForm.save()
            return redirect('home')
    return render(request, 'add_album.html', {'albumForm': albumForm})


def delete_album(request, id):
    album = Album.objects.get(pk=id)
    album.delete()
    return redirect('home')