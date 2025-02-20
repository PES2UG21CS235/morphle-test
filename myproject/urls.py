from django.contrib import admin
from django.urls import path
from app.views import htop

urlpatterns = [
    path('admin/', admin.site.urls),
    path('htop/', htop),
]