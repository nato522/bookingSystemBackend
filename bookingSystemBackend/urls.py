from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('bookingApp/', include('bookingApp.urls')),
    path('admin/', admin.site.urls),
]