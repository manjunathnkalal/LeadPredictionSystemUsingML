from django.test import TestCase

# Create your tests here.
from .models import Inputmodel

class InputmodelTest(TestCase):
    def test_model_creation(self):
        # Create a sample model instance
        lead = Inputmodel.objects.create(
            total_visits=5,
            total_time_spent_on_website=200,
            page_views_per_visit=3,
            lead_origin='API',
            lead_source='google',
            last_activity='Email Opened',
            specialization='E-Business',
            current_occupation='Student',
            tags='Already a student',
            lead_quality='High in Relevance',
            city='Mumbai',
            do_not_email='Yes',
            last_notable_activity='Approached upfront',
            free_copy_of_mastering_the_interview='No',
        )
        # Check instance creation
        self.assertIsNotNone(lead.id)

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

from django.test import TestCase
from leadpredict.forms import Inputform

class InputFormTest(TestCase):
    def test_form_valid_data(self):
        form_data = {
            'total_visits': 5,
            'total_time_spent_on_website': 200,
            'page_views_per_visit': 3,
            'lead_origin': 'API',
            'lead_source': 'google',
            'last_activity': 'Email Opened',
            'specialization': 'E-Business',
            'current_occupation': 'Student',
            'tags': 'Already a student',
            'lead_quality': 'High in Relevance',
            'city': 'Mumbai',
            'do_not_email': 'Yes',
            'last_notable_activity': 'Approached upfront',
            'free_copy_of_mastering_the_interview': 'No',
        }
        form = Inputform(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid_data(self):
        form_data = {}  # Empty data should make form invalid
        form = Inputform(data=form_data)
        self.assertFalse(form.is_valid())
