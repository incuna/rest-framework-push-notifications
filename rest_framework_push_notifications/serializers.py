from push_notifications import models
from rest_framework.serializers import HyperlinkedModelSerializer


class APNSDevice(HyperlinkedModelSerializer):
    class Meta:
        fields = ('url', 'registration_id', 'name', 'device_id', 'active')
        model = models.APNSDevice
