from django.shortcuts import render, get_object_or_404
from .models import Category, PortfolioProject


def portfolio_list(request, category_slug=None):
    categories = Category.objects.filter(is_active=True).only('id', 'name', 'slug')
    projects = PortfolioProject.objects.filter(is_published=True).select_related('category').only(
        'id', 'title', 'slug', 'cover_image', 'location', 'event_date', 'category__name'
    )
    selected_category = None

    if category_slug:
        selected_category = get_object_or_404(Category, slug=category_slug, is_active=True)
        projects = projects.filter(category=selected_category)

    context = {
        'categories': categories,
        'projects': projects,
        'selected_category': selected_category,
    }
    return render(request, 'portfolio/portfolio_list.html', context)


def project_detail(request, slug):
    project = get_object_or_404(
        PortfolioProject.objects.select_related('category'),
        slug=slug,
        is_published=True
    )
    gallery_images = project.images.all().only('id', 'image', 'caption', 'order')

    context = {
        'project': project,
        'gallery_images': gallery_images,
    }
    return render(request, 'portfolio/project_detail.html', context)
