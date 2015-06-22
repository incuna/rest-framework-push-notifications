from push_notifications import models
from rest_framework.generics import CreateAPIView, RetrieveDestroyAPIView

from . import serializers


class CreateAPNSDevice(CreateAPIView):
    serializer_class = serializers.APNSDevice

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class APNSDeviceDetail(RetrieveDestroyAPIView):
    serializer_class = serializers.APNSDevice

    def get_queryset(self):
        return models.APNSDevice.objects.filter(user=self.request.user)
