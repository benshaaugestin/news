from . import views
from django.conf.urls import url


urlpatterns = [
                url(r'^subscribe/$',views.AddToSubscriptionList.as_view(), name='subscribe'),
                url(r'^activate/(?P<token>[0-9A-Za-z]{32})/$',views.ActivateSubscription.as_view(), name='activate'),
                url(r'^contact/$',views.contactView , name='contact'),
                url(r'^comment/(?P<pk>[-\d]+)', views.CommentsView.as_view(), name='refresh_post'),

              ]

