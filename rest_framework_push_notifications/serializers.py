from push_notifications import models
from rest_framework.serializers import ModelSerializer


class APNSDevice(ModelSerializer):
    class Meta:
        fields = ('registration_id', 'name', 'device_id', 'active')
        model = models.APNSDevice
