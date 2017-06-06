from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Gustavo Aguiar', cpf='12345678901', email='gusttavoaguiarr@gmail.com',
                    phone='44-99823-9052')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'gusttavoaguiarr@gmail.com']
        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Gustavo Aguiar',
            '12345678901',
            'gusttavoaguiarr@gmail.com',
            '44-99823-9052',
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
