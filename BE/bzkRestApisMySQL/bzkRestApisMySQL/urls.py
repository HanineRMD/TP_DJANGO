from django.contrib import admin
from django.urls import path, include  # Make sure include is imported

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/tutorials/', include('tutorials.urls')),  # Ensure this line is correct
]
