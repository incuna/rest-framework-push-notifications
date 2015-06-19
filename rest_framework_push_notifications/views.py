from push_notifications import models
from rest_framework.generics import CreateAPIView, DestroyAPIView

from . import serializers


class CreateAPNSDevice(CreateAPIView):
    serializer_class = serializers.APNSDevice

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DeleteAPNSDevice(DestroyAPIView):
    def get_queryset(self):
        return models.APNSDevice.objects.filter(user=self.request.user)
