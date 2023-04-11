from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from newspaper.models import Topic

TOPIC_URL = reverse("newspaper:topic-list")
NEWSPAPER_URL = reverse("newspaper:newspaper-list")
REDACTOR_URL = reverse("newspaper:redactor-list")

URL_LIST = [TOPIC_URL, NEWSPAPER_URL, REDACTOR_URL]


class PublicViewsListsTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_login_required(self):
        for url in URL_LIST:
            response = self.client.get(url)
            self.assertNotEqual(response.status_code, 200)
