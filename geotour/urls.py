from geotour import views
from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
	url(r'^$', views.home, name='home'),
	url(r'^results/(?P<tourId>\w+)/$', views.results, name='results'),
	url(r'^test/', views.test, name='test'),
	url(r'^change/', views.change, name='change'),
)