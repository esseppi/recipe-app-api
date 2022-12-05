from django.contrib import admin
from django.urls import path
from dfr_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
]
