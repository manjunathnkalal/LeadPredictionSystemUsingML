from django.test import TestCase, Client
from django.urls import reverse
from leadpredict.models import Inputmodel

class PredictViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_predict_view_get(self):
        response = self.client.get(reverse('predict'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'leadpredict/inputform.html')
