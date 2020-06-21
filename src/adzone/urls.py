from __future__ import absolute_import

from adzone.views import ad_view
from django.conf.urls import url

urlpatterns = [
    url(r"^view/(?P<id>[\d]+)/$", ad_view, name="adzone_ad_view"),
]
