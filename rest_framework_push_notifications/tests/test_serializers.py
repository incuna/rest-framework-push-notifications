from django.test import TestCase

from .. import serializers


class TestAPNSDeviceSerializer(TestCase):
    def test_fields(self):
        expected = {'url', 'name', 'device_id', 'registration_id', 'active'}
        fields = serializers.APNSDevice().fields.keys()
        self.assertEqual(expected, set(fields))

    def test_registration_id(self):
        serializer = serializers.APNSDevice(data={'registration_id': 'test_id'})
        self.assertTrue(serializer.is_valid())

    def test_registration_id_required(self):
        serializer = serializers.APNSDevice(data={})
        self.assertFalse(serializer.is_valid())
