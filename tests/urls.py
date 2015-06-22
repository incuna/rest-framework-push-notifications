from django.conf.urls import include, url


urlpatterns = [
    url('', include('rest_framework_push_notifications.urls')),
]
