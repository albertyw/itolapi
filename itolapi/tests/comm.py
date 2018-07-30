from __future__ import unicode_literals
from mock import patch
import os
import tempfile
import unittest
import zipfile

from itolapi import Comm


class PullOutFilesTest(unittest.TestCase):

    def setUp(self):
        self.tempfile = tempfile.NamedTemporaryFile()

    def tearDown(self):
        self.tempfile.close()

    def test_tree_file_extension(self):
        zip_file = Comm.create_zip_from_files([self.tempfile.name])
        with open(zip_file.name, 'rb') as zip_file_handle:
            with zipfile.ZipFile(zip_file_handle) as zip_handle:
                files = zip_handle.namelist()
        expected_tree_name = os.path.basename(self.tempfile.name)
        self.assertIn(expected_tree_name, files)
        zip_file.close()


class UploadTreeTest(unittest.TestCase):

    def setUp(self):
        self.tempfile = tempfile.NamedTemporaryFile()
        self.files = [self.tempfile.name]
        self.comm = Comm()
        self.params = {'treeName': 'asdf'}

    def tearDown(self):
        self.tempfile.close()

    @patch('itolapi.comm.requests')
    @patch('itolapi.Comm.parse_upload')
    def test_upload_tree(self, mock_parse, mock_requests):
        mock_requests.post().text = 'asdf'
        mock_parse.return_value = 'qwer'
        output = self.comm.upload_tree(self.files, self.params)
        self.assertEqual(
            mock_requests.post.call_args[0][0],
            self.comm.upload_url
        )
        self.assertEqual(mock_requests.post.call_args[1]['data'], self.params)
        self.assertTrue('zipFile' in mock_requests.post.call_args[1]['files'])
        mock_parse.assert_called_once_with()
        self.assertEqual(self.comm.upload_output, 'asdf')
        self.assertEqual(output, 'qwer')


class ParseUploadTest(unittest.TestCase):

    def setUp(self):
        self.comm = Comm()

    def test_successful(self):
        self.comm.upload_output = 'SUCCESS 1234'
        status = self.comm.parse_upload()
        self.assertTrue(status)
        self.assertEqual(self.comm.warnings, [])
        self.assertEqual(self.comm.tree_id, '1234')

    def test_successful_warnings(self):
        self.comm.upload_output = "Warning 1\nWarning 2\nSUCCESS 1234"
        status = self.comm.parse_upload()
        self.assertTrue(status)
        self.assertEqual(self.comm.warnings, ['Warning 1', 'Warning 2'])
        self.assertEqual(self.comm.tree_id, '1234')

    def test_fatal(self):
        self.comm.upload_output = "ERR 1234"
        status = self.comm.parse_upload()
        self.assertFalse(status)
        self.assertEqual(self.comm.warnings, ["ERR 1234"])
        self.assertEqual(self.comm.tree_id, '')


class ExportImageTest(unittest.TestCase):

    def setUp(self):
        self.comm = Comm()
        self.params = {'tree_id': '1234'}

    @patch('itolapi.comm.requests')
    def test_export_image(self, mock_requests):
        mock_requests.post().content = 'asdf'
        output = self.comm.export_image(self.params)
        self.assertEqual(output, 'asdf')
