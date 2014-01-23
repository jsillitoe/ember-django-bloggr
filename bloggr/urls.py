from django.conf.urls import patterns, include, url
from django.contrib import admin
from bloggrdata.views import PostList, PostDetail
from bloggrember.views import HomeView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^post/(?P<pk>\d+)/$', PostDetail.as_view()),
    url(r'^posts/$', PostList.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomeView.as_view()),
)
