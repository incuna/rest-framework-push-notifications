from push_notifications.models import APNSDevice
from rest_framework import status

from tests.utils import APIRequestTestCase
from .. import views


class TestCreateAPNSDevice(APIRequestTestCase):
    view = views.CreateAPNSDevice

    def test_post(self):
        registration_id = 'test_id'
        data = {'registration_id': registration_id}

        request = self.create_request('post', data=data)
        view = self.get_view()
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        device = APNSDevice.objects.get()
        self.assertEqual(device.registration_id, registration_id)
        self.assertEqual(device.user, request.user)

    def test_duplicate(self):
        registration_id = 'test_id'
        APNSDevice.objects.create(registration_id='test_id')
        data = {'registration_id': registration_id}

        request = self.create_request('post', data=data)
        view = self.get_view()
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TestDeleteAPNSDevice(APIRequestTestCase):
    view = views.DeleteAPNSDevice

    def test_delete(self):
        user = self.user_factory.create()
        device = APNSDevice.objects.create(registration_id='test_id', user=user)

        request = self.create_request('delete', user=user)
        view = self.get_view()
        response = view(request, pk=device.pk)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        with self.assertRaises(APNSDevice.DoesNotExist):
            device.refresh_from_db()

    def test_delete_other_user_device(self):
        other_user = self.user_factory.create()
        device = APNSDevice.objects.create(registration_id='test_id', user=other_user)

        request = self.create_request('delete')
        view = self.get_view()
        response = view(request, pk=device.pk)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
