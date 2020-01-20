from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    # /music/
    # path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),
    # /music/id/
    # path('<int:album_id>/', views.detail,name='detail'),
    # path('<int:album_id>/', views.DetailView.as_view(), name='detail'),
    path(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    # /music/id/favorite
    # path('<int:album_id>/favorite/', views.favorite, name='favorite'),

    # /music/album/add
    path(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),

]