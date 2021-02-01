from django.http import response
from django.test import TestCase
from django.test.testcases import SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView


# Create your tests here.
class HomePageTests(SimpleTestCase):
    def setUp(self):
        url = reverse("home")
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_url(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homwpage_template(self):
        self.assertTemplateUsed(self.response, "home.html")

    def test_homepage_cotains_correct_html(self):
        self.assertContains(self.response, "Homepage")

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "Hi! there! I shold not be the page")

    def test_home_page_resolves_homepage_view(self):
        view = resolve("/")
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)
