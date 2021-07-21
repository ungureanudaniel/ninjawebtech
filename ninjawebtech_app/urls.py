from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from django.views.generic.base import TemplateView
from .views import homeview, reviewview, bloglistview

urlpatterns = [
    path('', homeview, name='home'),
    path('review/', reviewview, name='review'),
    path('blog/', bloglistview, name='blog'),





]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
