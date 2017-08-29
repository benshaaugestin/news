"""newsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.http import HttpResponse

from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
from news.sitemaps import NewsSitemap,CategorySitemap
from django.contrib.flatpages.views import flatpage
from django.conf.urls.static import static
from . import settings


# Your other patterns here
sitemaps= {'news':NewsSitemap,'category':CategorySitemap}

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include('news.urls')),
    url(r'^user/',include('user.urls')),
    url(r'^widgets/',include('widgets.urls')),
    url(r'^pages/', include('django.contrib.flatpages.urls',)),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^robots.txt$', TemplateView.as_view(template_name="robots.txt", content_type="text/plain"), name="robots_file"),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


