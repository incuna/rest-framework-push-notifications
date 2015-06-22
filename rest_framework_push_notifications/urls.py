from django.conf.urls import url

from . import views


urlpatterns = [
    url(
        r'^apns-device/$',
        views.CreateAPNSDevice.as_view(),
        name='apnsdevice-create',
    ),
    url(
        r'^apns-device/(?P<pk>\d+)/$',
        views.APNSDeviceDetail.as_view(),
        name='apnsdevice-detail',
    ),
]
