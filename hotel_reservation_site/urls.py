from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hotel/', include("hotel_app.urls")),
    path('api/', include("rest_framework.urls")),
    path('accounts/', include('accounts.urls')),
]

