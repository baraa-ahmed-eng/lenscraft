from django.db import models

class PhotographerProfile (models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=150)
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='profile/')
    location = models.TextField()
    experience = models.TextField()
    phone = models.CharField(max_length=20)
    whatsapp = models.CharField(max_length=20, blank=True)
    instagram = models.CharField(max_length=100, blank=True)
    telegram = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class Service(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    icon_name = models.CharField(max_length=50, blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order','id']

    def __str__(self):
        return self.title
