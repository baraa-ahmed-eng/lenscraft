from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from PIL import Image


# Maximum allowed file sizes
MAX_IMAGE_SIZE = 35 * 1024 * 1024  # 35 MB
MAX_VIDEO_SIZE = 250 * 1024 * 1024  # 250 MB


# Allowed image formats
validate_image_extension = FileExtensionValidator(
    allowed_extensions=['jpg', 'jpeg', 'png', 'webp'],
    message='Only JPG, JPEG, PNG, and WebP images are allowed.',
)


# Allowed video format
validate_video_extension = FileExtensionValidator(
    allowed_extensions=['mp4'],
    message='Only MP4 video files are allowed.',
)


def validate_image_size(value):
    """Ensure image size does not exceed 35 MB."""
    if value.size > MAX_IMAGE_SIZE:
        raise ValidationError(
            'Image file size must not exceed 35 MB.'
        )


def validate_video_size(value):
    """Ensure video size does not exceed 250 MB."""
    if value.size > MAX_VIDEO_SIZE:
        raise ValidationError(
            'Video file size must not exceed 250 MB.'
        )


def validate_image_content(value):
    """Verify that the uploaded file contains a valid image."""
    try:
        with Image.open(value) as image:
            image.verify()

    except Exception as exc:
        raise ValidationError(
            'The uploaded file is not a valid image.'
        ) from exc

    finally:
        # Reset the file pointer so Django can read the file again.
        if hasattr(value, 'seek'):
            value.seek(0)