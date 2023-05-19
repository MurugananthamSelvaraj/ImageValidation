from django.db import models


class Images(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image_file = models.ImageField(upload_to='images/', null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    binaryimage = models.BinaryField(editable=True, null=True)

    def __str__(self):
        return self.title
