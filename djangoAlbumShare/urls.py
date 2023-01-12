"""djangoAlbumShare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.album_share, name='album_share')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='album_share')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls import path, include
import albumShare

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path("", include("authentication.urls")),  # Auth routes - login / register

                  # ADD NEW Routes HERE

                  path("", include("albumShare.urls")),
                  path("api/", include("api.urls"))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
