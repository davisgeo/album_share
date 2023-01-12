from django.urls import path, re_path
from . import views

urlpatterns = [

    # The album_share page
    path('', views.index, name='home'),
    path('my_albums', views.my_albums, name='my_albums'),
    path('new_album', views.new_album, name='new_album'),
    path('edit_album/<int:pk>/', views.edit_album, name='edit_album'),
    path('view_album/<int:pk>/', views.view_album, name='view_album'),
    path('add_photo/<int:pk>/', views.new_photo, name='add_photo'),
    path('edit_photo/<int:pk>/', views.edit_photo, name='edit_photo'),
    path('delete_photo/<int:pk>/', views.delete_photo, name='delete_photo'),

]
