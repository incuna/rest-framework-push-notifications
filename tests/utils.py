from incuna_test_utils.testcases.api_request import BaseAPIRequestTestCase

from . import factories


class APIRequestTestCase(BaseAPIRequestTestCase):
    user_factory = factories.UserFactory
