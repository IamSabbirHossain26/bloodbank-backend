from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Blog(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)  # ✅ auto generate slug
    content = models.TextField()
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name="blogs")
    image = models.ImageField(upload_to="blogs/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:  # ✅ slug auto create if empty
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
