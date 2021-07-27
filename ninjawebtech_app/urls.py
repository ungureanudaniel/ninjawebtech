from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from django.views.generic.base import TemplateView
from .views import homeview, reviewview, bloglistview
from django.contrib.sitemaps.views import sitemap
from .sitemaps import ProjectCategorySitemap, ServiceSitemap, SkillSitemap, PortfolioSitemap, StaticSitemap
from django.views.generic.base import TemplateView
# app_name = "ninjawebtech_app"

sitemaps = {
    'ProjectCategory':ProjectCategorySitemap,
    'Service': ServiceSitemap,
    'Skill': SkillSitemap,
    'Portfolio': PortfolioSitemap,
    'static': StaticSitemap
}


urlpatterns = [
    path('', homeview, name='home'),
    path('review/', reviewview, name='review'),
    path('blog/', bloglistview, name='blog'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path("robots.txt", TemplateView.as_view(template_name="ninjawebtech_app/robots.txt", content_type="text/plain")),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
