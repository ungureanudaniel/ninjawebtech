from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from django.views.generic.base import TemplateView
from .views import homeview, reviewview, subscription_conf_view, \
hide_review_view, PostDetailView, BlogList, ArticleMonthArchiveView, \
search_results
from django.contrib.sitemaps.views import sitemap
from .sitemaps import ProjectCategorySitemap, ServiceSitemap, SkillSitemap,  StaticSitemap, PortfolioSitemap
from django.conf.urls.i18n import i18n_patterns
# app_name = "ninjawebtech_app"

sitemaps = {
    'ProjectCategory':ProjectCategorySitemap,
    'Service': ServiceSitemap,
    'Skill': SkillSitemap,
    'Portfolio': PortfolioSitemap,
    'static': StaticSitemap
}


urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('', homeview, name='home'),
    path('review/', reviewview, name='review'),
    path('hide_review/<int:pk>', hide_review_view, name='hide_review'),
    path('search_results/', search_results, name='search_results'),
    path('blog-list/', BlogList.as_view(), name='blog_list'),
    path('blog/<slug:slug>/', PostDetailView.as_view(), name='blog_detail'),
    path('hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount')),
    path('<int:year>/<int:month>/', ArticleMonthArchiveView.as_view(month_format='%m'), name="post_archive_month"),
    path('subscription_confirmation/', subscription_conf_view, name='subscription_confirmation'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path("robots.txt", TemplateView.as_view(template_name="ninjawebtech_app/robots.txt", content_type="text/plain")),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
