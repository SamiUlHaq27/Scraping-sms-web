from django.contrib.sitemaps import Sitemap
from nums.models import Country, Number
from django.contrib.sites.models import Site


class CountriesSitemap(Sitemap):
    changefreq = "never"
    protocol = "https"
    
    def get_urls(self, site=None, **kwargs):
        site = Site(domain='temporay-sms-number.xyz', name='temporay-sms-number.xyz')
        return super(CountriesSitemap, self).get_urls(site=site, **kwargs)
    
    def items(self):
        return Country.objects.all()
    
    def lastmod(self, obj:Country):
        return obj.updated_at

class NumbersSitemap(Sitemap):
    protocol = "https"
    changefreq = "hourly"
    country = None
    
    def get_urls(self, site=None, **kwargs):
        site = Site(domain='temporay-sms-number.xyz', name='temporay-sms-number.xyz')
        return super(NumbersSitemap, self).get_urls(site=site, **kwargs)
    
    def items(self):
        return Number.objects.filter(country_slug=self.country)
    
    def lastmod(self, obj:Number):
        return obj.updated_at
    

    