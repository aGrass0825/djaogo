from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^index/$', views.index, name="ind"),
    url(r'^sq/$', views.sq),
    url(r'^weather/(?P<city>\w+)/(?P<year>\d{4})/$', views.weather),
    url(r'^body/$', views.get_body),
    url(r'^jsondata/$', views.get_body_json),
    url(r'^headers/$', views.get_headers),
    url(r'^others/$', views.others),
    url(r'^response/$', views.response),
    url(r'^subresponse/$', views.subresponse),
    url(r'^jsonresponse/$', views.jsonresponse),
    url(r'^demo_views/$', views.demo_views),
    url(r'^cook/$', views.cook),
    url(r'^session/$', views.sessiondemo),
]