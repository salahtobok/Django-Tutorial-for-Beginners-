from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    # /music/
    path('', views.index, name='index'),
    # /music/id/
    # path(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
    path('<int:album_id>/', views.detail,name='detail'),

]