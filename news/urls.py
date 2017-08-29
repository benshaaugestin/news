from . import views
from django.conf.urls import url

app_name = 'news'
urlpatterns = [
    url(r'^rand/(?P<num>[-\d]+)/', views.rand),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/category/$', views.CategoryView.as_view(), name='category'),
    url(r'^search/$',views.SearchResultView.as_view(),name='search_result')
    ]

