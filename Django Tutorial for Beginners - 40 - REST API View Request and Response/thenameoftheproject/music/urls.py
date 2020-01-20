from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    # /music/
    # path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),

    # register
    path('register/', views.UserFormView.as_view(), name='register'),


    # /music/id/
    path(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),

    # /music/id/favorite
    # path('<int:album_id>/favorite/', views.favorite, name='favorite'),

    # /music/album/add
    path(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),

    # /music/album/1
    path('album/<pk>/', views.AlbumUpdate.as_view(), name='album-update'),

    # /music/album/1/delete

    path(r'album/(?P<pk>\d+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),
]