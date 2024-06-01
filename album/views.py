from django.shortcuts import render, redirect
from . import forms
from . import models

def add(request):
    if request.method == 'POST':
        form = forms.AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = forms.AlbumForm()

    return render(request, 'add-album.html', {'form': form})

def edit(request, id):
    album = models.Album.objects.get(pk=id)
    form = forms.AlbumForm(instance=album)

    if request.method == 'POST':
        form = forms.AlbumForm(request.POST, instance=album )
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'edit-album.html', {'form': form})

def delete(request, id):
    album = models.Album.objects.get(pk=id)
    album.delete()
    return redirect('home')