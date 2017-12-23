from django.conf.urls import url,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	url(r'^$', views.home, name='home'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),  # <--

    url(r'^$', views.index, name='index'),
    url(r'^post/', views.index,name='index'),
    url(r'^(?P<Post_id>[0-9]+)/$', views.detail, name='detail'),
]
