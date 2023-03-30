from django.test import TestCase
from django.utils import timezone
from newspaper.models import Newspaper, Redactor, Topic


class NewspaperModelTestCase(TestCase):
    def setUp(self):
        self.topic = Topic.objects.create(name="Sports")
        self.redactor1 = Redactor.objects.create(username="John")
        self.redactor2 = Redactor.objects.create(username="Jane")
        self.newspaper = Newspaper.objects.create(
            title="Test Newspaper",
            content="This is a test newspaper.",
            topic=self.topic,
            image="test_image.jpg",
        )
        self.newspaper.publishers.set([self.redactor1, self.redactor2])

    def test_newspaper_model_string_representation(self):
        self.assertEqual(str(self.newspaper), "Test Newspaper")

    def test_newspaper_model_publishers(self):
        self.assertEqual(self.newspaper.publishers.count(), 2)
        self.assertIn(self.redactor1, self.newspaper.publishers.all())
        self.assertIn(self.redactor2, self.newspaper.publishers.all())

    def test_newspaper_model_published_date(self):
        self.assertAlmostEqual(
            self.newspaper.published_date,
            timezone.now(),
            delta=timezone.timedelta(seconds=1),
        )


class TopicModelTestCase(TestCase):
    def setUp(self):
        self.topic = Topic.objects.create(
            name="Test Topic",
            short_description="This is a test topic.",
            image="test_image.jpg",
        )

    def test_topic_model_string_representation(self):
        self.assertEqual(str(self.topic), "Test Topic")

    def test_topic_model_date_added(self):
        self.assertAlmostEqual(
            self.topic.date_added,
            timezone.now(),
            delta=timezone.timedelta(seconds=1),
        )


class RedactorModelTestCase(TestCase):
    def setUp(self):
        self.redactor = Redactor.objects.create(
            username="testuser",
            first_name="Test",
            last_name="User",
            email="testuser@example.com",
            years_of_experience=2.5,
        )

    def test_redactor_model_string_representation(self):
        self.assertEqual(str(self.redactor), "Test User 2.5")

    def test_redactor_model_get_full_name(self):
        self.assertEqual(self.redactor.get_full_name(), "Test User")