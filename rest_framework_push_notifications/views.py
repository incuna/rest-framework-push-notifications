from push_notifications import models
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from . import serializers


class APNSDeviceList(ListCreateAPIView):
    serializer_class = serializers.APNSDevice

    def get_queryset(self):
        return models.APNSDevice.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class APNSDeviceDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.APNSDeviceUpdate

    def get_queryset(self):
        return models.APNSDevice.objects.filter(user=self.request.user)
