from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.portfolio_list, name='list'),
    path('category/<slug:category_slug>/', views.portfolio_list, name='category_filter'),
    path('project/<slug:slug>/', views.project_detail, name='detail'),
]