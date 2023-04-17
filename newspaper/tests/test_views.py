from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from newspaper.models import Topic, Newspaper

TOPIC_URL = reverse("newspaper:topic-list")
NEWSPAPER_URL = reverse("newspaper:newspaper-list")
REDACTOR_URL = reverse("newspaper:redactor-list")
TOPIC_CREATE_URL = reverse("newspaper:topic-create")
NEWSPAPER_CREATE_URL = reverse("newspaper:newspaper-create")

URL_LIST = [TOPIC_URL, NEWSPAPER_URL, REDACTOR_URL]


class PublicViewsListsTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_login_required(self):
        for url in URL_LIST:
            response = self.client.get(url)
            self.assertNotEqual(response.status_code, 200)


class TestTopicCRUDFunctionality(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username="testerTopic",
            email="testertopic@tester.com",
            password="1qazcde3",
        )
        self.client.force_login(self.user)
        Topic.objects.create(name="Test topic2", short_description="Test short description2")

    def test_topic_create(self):
        payload = {
            "name": "Test topic",
            "short_description": "Test short description",
        }
        self.client.post(TOPIC_CREATE_URL, data=payload)
        exists = Topic.objects.filter(name="Test topic").exists()
        self.assertTrue(exists)

    def test_update_topic(self):
        topic = Topic.objects.get(name="Test topic2")
        payload = {
            "name": "Test topic2Updated",
            "short_description": "Test short description2",
        }
        url = reverse("newspaper:topic-update", args=[topic.id])
        self.client.post(url, data=payload)
        topic.refresh_from_db()
        self.assertEqual(topic.name, payload["name"])
        self.assertEqual(topic.short_description, payload["short_description"])

    def test_topic_delete(self):
        topic = Topic.objects.get(name="Test topic2")
        url = reverse("newspaper:topic-delete", args=[topic.id])
        self.client.post(url)
        exists = Topic.objects.filter(name="Test topic2").exists()
        self.assertFalse(exists)

    def test_topic_list(self):
        response = self.client.get(TOPIC_URL)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test topic2")
        self.assertTemplateUsed(response, "newspaper/newspaper_lists/topic_list.html")


class TestNewspaperCRUDFunctionality(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username="testerNewspaper",
            email="testernewspaper@tester.com",
            password="1qazcde3",
        )
        self.client.force_login(self.user)
        Topic.objects.create(name="Test topic", short_description="Test short description")
        Newspaper.objects.create(
            title="Test newspaperTitle",
            content="Test content2",
            topic=Topic.objects.get(name="Test topic"),
        )

    def test_newspaper_create(self):
        payload = {
            "title": "Test newspaperTitle",
            "content": "Test content",
            "topic": Topic.objects.get(name="Test topic").id,
        }
        self.client.post(NEWSPAPER_CREATE_URL, data=payload)
        exists = Newspaper.objects.filter(title="Test newspaperTitle").exists()
        self.assertTrue(exists)

    def test_update_newspaper(self):
        newspaper = Newspaper.objects.get(title="Test newspaperTitle")
        payload = {
            "title": "Test newspaperTitleUpdated",
            "content": "Test content2",
            "topic": Topic.objects.get(name="Test topic").id,
            "publishers": self.user.id,
        }
        url = reverse("newspaper:newspaper-update", args=[newspaper.id])
        self.client.post(url, data=payload)
        newspaper.refresh_from_db()
        self.assertEqual(newspaper.title, payload["title"])
        self.assertEqual(newspaper.content, payload["content"])

    def test_newspaper_delete(self):
        newspaper = Newspaper.objects.get(title="Test newspaperTitle")
        url = reverse("newspaper:newspaper-delete", args=[newspaper.id])
        self.client.post(url)
        exists = Newspaper.objects.filter(title="Test newspaperTitle").exists()
        self.assertFalse(exists)

    def test_newspaper_list(self):
        response = self.client.get(NEWSPAPER_URL)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test newspaperTitle")
        self.assertTemplateUsed(response, "newspaper/newspaper_lists/newspaper_list.html")
