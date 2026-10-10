from django.db import models

from .validators import (
    validate_image_extension,
    validate_image_size,
    validate_image_content,
    validate_video_extension,
    validate_video_size,
)


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, unique=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return self.name


class PortfolioProject(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='projects',
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True)
    description = models.TextField(blank=True)

    cover_image = models.ImageField(
        upload_to='portfolio/cover/',
        validators=[
            validate_image_extension,
            validate_image_size,
            validate_image_content,
        ],
    )

    video_clip = models.FileField(
        upload_to='portfolio/videos/',
        blank=True,
        null=True,
        validators=[
            validate_video_extension,
            validate_video_size,
        ],
    )

    event_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=200, blank=True)
    is_featured = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class PortfolioImage(models.Model):
    project = models.ForeignKey(
        PortfolioProject,
        on_delete=models.CASCADE,
        related_name='images',
    )

    image = models.ImageField(
        upload_to='portfolio/gallery/',
        validators=[
            validate_image_extension,
            validate_image_size,
            validate_image_content,
        ],
    )

    caption = models.CharField(max_length=200, blank=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return f"{self.project.title} - {self.id}"