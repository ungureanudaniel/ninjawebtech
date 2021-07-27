from django.contrib.sitemaps import Sitemap
from .models import ProjectCategory, Service, Skill, Portfolio, Post
from django.urls import reverse
from slugify import slugify

class ProjectCategorySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return ProjectCategory.objects.all()

    def location(self, item):
        return item

    def location(self,obj):
        return '/%s' % (obj.title)

class ServiceSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return Service.objects.all()

    def location(self, item):
        return item

    def location(self,obj):
        return '/%s' % (obj.title)

class SkillSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return Skill.objects.all()

    def location(self, item):
        return item

    def location(self,obj):
        return '/%s' % (obj.title)

class PortfolioSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return Portfolio.objects.all()

    def location(self, item):
        return item

    def location(self,obj):
        return '/%s' % (obj.title)
        
class StaticSitemap(Sitemap):
    changefreq = "yearly"

    def items(self):
        return ['blog']

    def location(self, item):
        return reverse(item)
