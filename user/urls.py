from . import views
from django.conf.urls import url,include
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^profile/$', login_required(views.UpdateView.as_view()), name='profile'),
    url(r'^setpassword/', views.change_password, name='set_password'),

    url(r'^oauth/', include('social_django.urls', namespace='social')),

    url(r'^password_reset/$', auth_views.password_reset,
        {'template_name': 'registration/pswd_reset_form.html'}, name='password_reset'),

    url(r'^password_reset/done/$', auth_views.password_reset_done,
        {'template_name': 'registration/pswd_reset_done.html', }, name='password_reset_done'),

    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})',
        auth_views.password_reset_confirm,
        {'template_name': 'registration/pswd_reset_confirm.html', }, name='password_reset_confirm'),

    url(r'^reset/done/$', auth_views.password_reset_complete,
        {'template_name': 'registration/pswd_reset_complete.html'}, name='password_reset_complete')

]