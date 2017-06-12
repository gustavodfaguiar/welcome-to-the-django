from datetime import datetime
from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Gustavo Aguiar',
            cpf='12345678901',
            email='gusttavoaguiarr@gmail.com',
            phone='44-998239052'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at_(self):
        """Subscription must have an auto created_at attr."""
        self.assertIsInstance(self.obj.created_at, datetime)
    
    def test_str(self):
        self.assertEqual('Gustavo Aguiar', str(self.obj))
