from django.shortcuts import render
from.models import PhotographerProfile, Service
from portfolio.models import PortfolioProject

def home(request):
    profile = PhotographerProfile.objects.first()
    services = Service.objects.filter(is_active=True)
    featured_projects = PortfolioProject.objects.filter(is_published=True,is_featured=True)
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