from django.shortcuts import render
from django.views.generic import ListView, DetailView

from uploadimage_app.models import Image

class HomeView(ListView):
    model = Image
    template_name = 'home.html'
    context_object_name = 'posts'
    
    def get_queryset(self):
        # Get all images ordered by the 'updated_at' field in descending order
        return Image.objects.all().order_by('-updated_at')

class ImageDetailView(DetailView):
    model = Image
    template_name = 'image_detail.html'
    context_object_name = 'post'
    
    def get_context_data(self, **kwargs):
        # Get the base context
        context = super().get_context_data(**kwargs)
        # Add more images to the context
        context['more_images'] = Image.objects.all().order_by('-updated_at')[:10]
        return context
