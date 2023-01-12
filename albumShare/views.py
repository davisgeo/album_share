from django.shortcuts import render

# Create your views here.


from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from albumShare.models import Album


@login_required(login_url="/login/")
def index(request):
    all_public_albums = Album.objects.filter(private=False)
    context = {
        'page': 'home',
        'all_public_albums': all_public_albums
    }

    html_template = loader.get_template('album_share/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def my_albums(request):
    all_my_albums = Album.objects.filter(user_id=request.user.id)
    context = {
        'page': 'my_albums',
        'all_my_albums': all_my_albums
    }

    html_template = loader.get_template('album_share/my_albums.html')
    return HttpResponse(html_template.render(context, request))
