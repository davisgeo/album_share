from django.urls import path, re_path
from . import views

urlpatterns = [

    # The album_share page
    path('', views.index, name='home'),
    path('my_albums', views.my_albums, name='my_albums')

]
