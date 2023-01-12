from django.shortcuts import render
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .forms import *
from albumShare.models import Album


# Create your views here.

@login_required(login_url="/login/")
def index(request):
    all_public_albums = Album.objects.filter(private=False).order_by('-id')
    context = {
        'page': 'home',
        'all_public_albums': all_public_albums
    }

    html_template = loader.get_template('album_share/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def my_albums(request):
    all_my_albums = Album.objects.filter(user_id=request.user.id)
    for item in all_my_albums:
        print(item.cover_photo_url)
    context = {
        'page': 'my_albums',
        'all_my_albums': all_my_albums
    }

    html_template = loader.get_template('album_share/my_albums.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def new_album(request):
    form = AlbumForm()
    all_my_albums = Album.objects.filter(user_id=request.user.id)
    if request.method == 'POST':
        form = AlbumForm(request.POST or None)

        if form.is_valid():
            # extra steps
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return HttpResponseRedirect('/edit_album/' + str(obj.id) + '/')
    context = {
        'page': 'my_albums',
        'all_my_albums': all_my_albums,
        'form': form,
        'edit': False
    }

    html_template = loader.get_template('album_share/edit_album.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def edit_album(request, pk=None):
    album = Album.objects.get(pk=pk)
    photos = None
    try:
        photos = Photo.objects.filter(album=album)
    except:
        pass
    form = AlbumForm(instance=album)

    if request.method == 'POST':

        if form.is_valid():
            # extra steps
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            form = AlbumForm(instance=obj)
    context = {
        'page': 'my_albums',
        'album': album,
        'photos': photos,
        'form': form,
        'edit': True
    }

    html_template = loader.get_template('album_share/edit_album.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def new_photo(request, pk):
    album = Album.objects.get(pk=pk)
    form = PhotoForm()
    if request.method == 'POST':
        form = PhotoForm(request.POST or None)

        if form.is_valid():
            # extra steps
            obj = form.save(commit=False)
            obj.photo = request.FILES['photo']
            obj.album = album
            obj.save()
            if obj.album_cover:
                album.cover_photo_url = obj.photo.url
                album.save()
            return HttpResponseRedirect('/edit_album/' + str(pk) + '/')
    context = {
        'page': 'my_albums',
        'album': album,
        'form': form
    }

    html_template = loader.get_template('album_share/add_photo.html')
    return HttpResponse(html_template.render(context, request))
