from django.shortcuts import render, redirect
from .forms import MusicianForm
from .models import Musician

# Create your views here.
def add_musician(request):
    if request.method == 'POST':
        musicianForm = MusicianForm(request.POST)
        if musicianForm.is_valid():
            musicianForm.save()
            return redirect('add_musician')
    else:
        musicianForm = MusicianForm()
    return render(request, 'add_musician.html', {'musicianForm': musicianForm})


def edit_musician(request, id):
    musician = Musician.objects.get(pk= id)
    musicianForm = MusicianForm(instance=musician)
    if request.method == 'POST':
        musicianForm = MusicianForm(request.POST, instance=musician)
        if musicianForm.is_valid():
            musicianForm.save()
            return redirect('home')
    return render(request, 'add_musician.html', {'musicianForm': musicianForm})


def delete_musician(request,id):
    musician = Musician.objects.get(pk= id)
    musician.delete()
    return redirect('home')
    