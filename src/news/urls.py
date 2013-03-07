from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from models import News


urlpatterns = patterns(
    '', 
    url(r'^$', ListView.as_view(model=News), name='news.list'),
    url(r'^(?P<slug>[-_\w]+)/$', DetailView.as_view(model=News), name='news.detail'),
)


