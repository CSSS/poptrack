from django.conf.urls import patterns, include, url


from poptrack import views

urlpatterns = patterns('',
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'add/$', views.AddFilling, name='add'),
	url(r'stock/$', views.ViewStock, name='stock'),
)

urlpatterns += patterns('django.contrib.auth.views',
        (r'^login/$',           'login',  {
                'template_name': 'login.html'}),
        (r'^logout/$',          'logout', {
                'template_name': 'logout.html'}),
)

