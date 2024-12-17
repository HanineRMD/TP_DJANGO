from django.urls import path
from tutorials import views

urlpatterns = [
    path('', views.tutorial_list),  # Handles GET, POST, DELETE for /api/tutorials/
    path('<int:pk>/', views.tutorial_detail),  # Handles GET, PUT, DELETE for /api/tutorials/<id>/
    path('published/', views.tutorial_list_published),  # Handles GET for /api/tutorials/published/
]
