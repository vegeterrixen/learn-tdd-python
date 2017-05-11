from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest


class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
