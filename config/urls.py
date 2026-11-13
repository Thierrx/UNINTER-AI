from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('ia/', include('assistant.urls')),
    path('navegador/', include('integrations.urls')),
    path('materiais/', include('academics.urls')),
]