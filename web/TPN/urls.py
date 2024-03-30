"""
URL configuration for TPN project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from .views import mysitemap_func

from nums.mysitemaps import CountriesSitemap, NumbersSitemap

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('nums.urls')),
    path('countries/sitemap.xml', sitemap, {'sitemaps':{"country":CountriesSitemap}}),
    path('country/<country>/sitemap.xml', mysitemap_func, {'sitemaps':{"numbers":NumbersSitemap}})
]


handler404 = 'nums.views.error_404_view'