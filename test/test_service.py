from unittest import TestCase
from service import service
from unittest.mock import patch, MagicMock
from os.path import join, dirname
import psycopg2


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

    def test_execute(self):
        arquivo = join(dirname(__file__), 'file_test')
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        with open(arquivo, 'r+') as file:
            service.execute(file, mock_conn)


class TestDatabase(TestCase):

    @patch('psycopg2.connect')
    def test_get_user_by_id(self, mock_connect):
        # Configurando o mock do cursor
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor