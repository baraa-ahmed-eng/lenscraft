from django.shortcuts import render
from.models import PhotographerProfile, Service
from portfolio.models import PortfolioProject

def home(request):
    profile = PhotographerProfile.objects.first()
    services = Service.objects.filter(is_active=True).only('id', 'title', 'description', 'icon_name')
    featured_projects = PortfolioProject.objects.filter(
        is_published=True,
        is_featured=True
    ).select_related('category').only(
        'id', 'title', 'slug', 'cover_image', 'location', 'event_date', 'category__name'
    )
    context = {
        'profile': profile,
        'services': services,
        'featured_projects': featured_projects
    }
    return render(request, 'core/home.html', context)

def contact(request):
    profile = PhotographerProfile.objects.first()
    context = {
        'profile': profile,
    }
    return render(request, 'core/contact.html', context)