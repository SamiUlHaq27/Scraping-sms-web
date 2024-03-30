from django.contrib.sitemaps.views import sitemap

def mysitemap_func(request, country, sitemaps):
    sitemaps["numbers"].country = country
    return sitemap(request, sitemaps)