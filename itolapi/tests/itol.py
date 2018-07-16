from __future__ import unicode_literals
from mock import MagicMock, patch
import unittest

from itolapi import Itol


class ItolTest(unittest.TestCase):

    def setUp(self):
        self.itol = Itol.Itol()

    def test_initializes(self):
        self.assertEqual(self.itol.variables, {})
        self.assertIsNotNone(self.itol.comm)

    def test_add_variable(self):
        self.itol.add_variable('x', 'asdf')
        self.assertEqual(self.itol.variables['x'], 'asdf')

    def test_checks_variable_name(self):
        with self.assertRaises(TypeError):
            self.itol.add_variable(1234, 'asdf')

    def test_checks_variable_value(self):
        with self.assertRaises(TypeError):
            self.itol.add_variable('x', 1234)

    def test_checks_file_variable(self):
        with self.assertRaises(IOError):
            self.itol.add_variable('File', ' ')

    def test_is_file(self):
        self.assertFalse(Itol.Itol.is_file('asdf'))
        self.assertTrue(Itol.Itol.is_file('asdfFile'))

    def test_good_upload(self):
        with patch('itolapi.Comm.Comm.upload_tree') as mock_upload:
            mock_upload.return_value = True
            self.itol.comm.tree_id = 1234
            self.assertEqual(self.itol.upload(), 1234)

    def test_bad_upload(self):
        with patch('itolapi.Comm.Comm.upload_tree') as mock_upload:
            mock_upload.return_value = False
            self.itol.comm.tree_id = 1234
            self.assertEqual(self.itol.upload(), 0)

    def test_get_itol_export(self):
        self.itol.comm.tree_id = 1234
        export = self.itol.get_itol_export()
        self.assertEqual(export.params['tree'], 1234)

    def test_print_variables(self):
        self.itol.print_variables()

    def test_delete_variables(self):
        self.itol.add_variable('asdf', '1234')
        self.assertTrue('asdf' in self.itol.variables)
        self.itol.delete_variable('asdf')
        self.assertFalse('asdf' in self.itol.variables)
        self.assertFalse('asdf' in self.itol.variables)  # Idempotent
