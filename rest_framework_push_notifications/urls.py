from django.conf.urls import url

from . import views


urlpatterns = [
    url(
        r'^apns-device/$',
        views.APNSDeviceList.as_view(),
        name='apnsdevice-list',
    ),
    url(
        r'^apns-device/(?P<pk>\d+)/$',
        views.APNSDeviceDetail.as_view(),
        name='apnsdevice-detail',
    ),
]
