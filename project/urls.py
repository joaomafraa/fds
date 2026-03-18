from django.contrib import admin
from django.urls import path

from django.url import include

urlpatterns = [
    path('forum/', include('forum.urls')),
    path('admin/', admin.site.urls),
]