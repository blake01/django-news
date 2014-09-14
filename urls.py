from django.conf.urls import patterns, url
from news.views import NewsListView, NewsArchiveView, NewsDetailView


urlpatterns = patterns('',
    url(r'^$', NewsListView.as_view(), name='article_list'),
    url(r'^(?P<year>[0-9]{4})/$', NewsArchiveView.as_view(), name='article_year_archive'),
    url(r'^(?P<slug>[\w-]+)/$', NewsDetailView.as_view(), name='article_detail'),
)
