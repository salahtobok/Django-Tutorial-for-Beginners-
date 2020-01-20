from django.shortcuts import render

# Create your views here.
from django.http import  HttpResponse
from django.shortcuts import  render
from .models import Album

def index(request):
    all_albums = Album.objects.all()
    context = {
        'all_albums' : all_albums,
    }
    return render(request,'music/index.html',context)

def detail(request,album_id):
  return HttpResponse("<h2>Details for Album id : "+str(album_id)+"</h2>")