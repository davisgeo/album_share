from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import AlbumSerializer, PhotoSerializer

from albumShare.models import Album, Photo


# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/album-list/',
        'Detail View': '/album-detail/<str:pk>/',
        'Photo List': '/photo-list/<str:pk>/',
        'Create': '/album-create/',
        'Update': '/album-update/<str:pk>/',
        'Delete': '/album-delete/<str:pk>/',
    }

    return Response(api_urls)


@api_view(['GET'])
def albumList(request):
    albums = Album.objects.all().order_by('-id')
    serializer = AlbumSerializer(albums, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def albumDetail(request, pk):
    albums = Album.objects.get(id=pk)
    serializer = AlbumSerializer(albums, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def photoList(request, pk):
    album = Album.objects.get(id=pk)
    photos = Photo.objects.get(album=album)
    serializer = PhotoSerializer(photos, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def albumCreate(request):
    serializer = AlbumSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def albumUpdate(request, pk):
    album = Album.objects.get(id=pk)
    serializer = AlbumSerializer(instance=album, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def albumDelete(request, pk):
    album = Album.objects.get(id=pk)
    album.delete()

    return Response('Item succsesfully delete!')
