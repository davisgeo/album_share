from django.urls import path, re_path
from . import views

urlpatterns = [

    # The album_share page
    path('', views.index, name='home'),
    path('my_albums', views.my_albums, name='my_albums'),
    path('new_album', views.new_album, name='new_album'),
    path('edit_album/<int:pk>/', views.edit_album, name='edit_album'),
    path('add_photo/<int:pk>/', views.new_photo, name='add_photo'),

]
