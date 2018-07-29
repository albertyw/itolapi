from __future__ import unicode_literals
from mock import patch
import unittest

from itolapi import ItolExport


class ItolTest(unittest.TestCase):

    def setUp(self):
        self.export = ItolExport()

    def test_add_export_param_dict(self):
        params = {'asdf': 'qwer'}
        self.export.add_export_param_dict(params)
        self.assertEqual(self.export.params, params)

    def test_set_export_param_value(self):
        params = {'asdf': 'qwer'}
        self.export.set_export_param_value('asdf', 'qwer')
        self.assertEqual(self.export.params, params)

    def test_get_export_params(self):
        params = {'asdf': 'qwer'}
        self.export.add_export_param_dict(params)
        self.assertEqual(self.export.get_export_params(), params)

    def test_export(self):
        with patch('itolapi.Comm.export_image') as mock_upload:
            mock_upload.return_value = b'asdf'
            self.export.export('/tmp/asdf.pdf')
