from unittest import TestCase
from service import service


class ServiceTest(TestCase):

    def test_is_valid_cpf(self):
        result = service._validate_cpf('73159409104')
        self.assertEqual(result, True)

    def test_is_invalid_cpf(self):
        result = service._validate_cpf('73159409105')
        self.assertEqual(result, False)

    def test_just_numbers(self):
        result = service._just_numbers('139.486.268-71')
        self.assertEqual(result, '13948626871')
