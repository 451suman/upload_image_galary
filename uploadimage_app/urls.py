from django.urls import path

from uploadimage_app import views

urlpatterns = [
path("", views.HomeView.as_view(), name="home"),
path("image-detail/<int:pk>/", views.ImageDetailView.as_view(), name="image-detail"),
]