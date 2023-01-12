from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('album-list/', views.albumList, name="album-list"),
    path('album-detail/<str:pk>/', views.albumDetail, name="album-detail"),
    path('photo-list/<str:pk>/', views.photoList, name="photo-list"),
    path('album-create/', views.albumCreate, name="album-create"),

    path('album-update/<str:pk>/', views.albumUpdate, name="album-update"),
    path('album-delete/<str:pk>/', views.albumDelete, name="album-delete"),
]
