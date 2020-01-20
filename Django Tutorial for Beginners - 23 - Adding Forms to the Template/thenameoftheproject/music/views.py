from django.shortcuts import render

# Create your views here.
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from .models import Album


def index(request):
    all_albums = Album.objects.all()
    context = {
        'all_albums': all_albums,
    }
    return render(request, 'music/index.html', context)


def detail(request, album_id):
    # album = Album.objects.get(pk=album_id)
    album = get_object_or_404(Album,pk=album_id)
    return render(request,'music/detail.html',{'album':album})

def favorite(request):
    return #