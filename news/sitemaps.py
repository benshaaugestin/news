from django.contrib.sitemaps import Sitemap
from news.models import News,Category

class NewsSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return News.objects.all()


class CategorySitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Category.objects.all()
