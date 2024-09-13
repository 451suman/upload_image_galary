from django.db import models

# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="post_images/%Y/%m/%d", blank=False)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title