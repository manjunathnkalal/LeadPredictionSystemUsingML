from django.test import TestCase
from leadpredict.models import Inputmodel

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
