from django.shortcuts import render, redirect
from . import forms
from . import models

def add(request):
    if request.method == 'POST':
        form = forms.MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = forms.MusicianForm()

    return render(request, 'add.html', {'form': form})

def edit(request, id):
    musician = models.Musician.objects.get(pk=id)
    form = forms.MusicianForm(instance=musician)

    if request.method == 'POST':
        form = forms.MusicianForm(request.POST, instance=musician )
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'edit.html', {'form': form})

def delete(request, id):
    musician = models.Musician.objects.get(pk=id)
    musician.delete()
    return redirect('home')