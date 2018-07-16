from __future__ import unicode_literals
from mock import MagicMock, patch
import tempfile
import unittest

from itolapi import Comm


class PullOutFilesTest(unittest.TestCase):

    def setUp(self):
        self.tempfile = tempfile.TemporaryFile()

    def tearDown(self):
        self.tempfile.close()

    def test_pull_out_files(self):
        params = {}
        params['asdf'] = 'qwer'
        params['zxcv'] = self.tempfile
        new_params, files = Comm.Comm.pull_out_files(params)
        self.assertEqual(new_params, {'asdf': 'qwer'})
        self.assertEqual(files, {'zxcv': params['zxcv']})

    def test_doesnt_modify_params(self):
        params = {}
        params['asdf'] = 'qwer'
        params['zxcv'] = self.tempfile
        Comm.Comm.pull_out_files(params)
        self.assertTrue('asdf' in params)
        self.assertTrue('zxcv' in params)


class UploadTreeTest(unittest.TestCase):

    def setUp(self):
        self.tempfile = tempfile.NamedTemporaryFile()
        self.comm = Comm.Comm()
        self.params = {'asdf': 'qwer'}
        self.files = {'zxcv': self.tempfile}
        self.all_params = self.params.copy()
        self.all_params.update(self.files)

    def tearDown(self):
        self.tempfile.close()

    @patch('itolapi.Comm.Comm.pull_out_files')
    @patch('itolapi.Comm.requests')
    @patch('itolapi.Comm.Comm.parse_upload')
    def test_upload_tree(self, mock_parse, mock_requests, mock_pull):
        mock_pull.return_value = (self.params, self.files)
        mock_requests.post().text = 'asdf'
        mock_parse.return_value = 'qwer'
        output = self.comm.upload_tree(self.all_params)
        mock_pull.assert_called_once_with(self.all_params)
        self.assertEqual(mock_requests.post.call_args[0][0], self.comm.upload_url)
        self.assertEqual(mock_requests.post.call_args[1]['data'], self.params)
        self.assertTrue('zipFile' in mock_requests.post.call_args[1]['files'])
        mock_parse.assert_called_once_with()
        self.assertEqual(self.comm.upload_output, 'asdf')
        self.assertEqual(output, 'qwer')


class ParseUploadTest(unittest.TestCase):

    def setUp(self):
        self.comm = Comm.Comm()

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
        self.comm = Comm.Comm()
        self.params = {'tree_id': '1234'}
        self.files = {}

    @patch('itolapi.Comm.Comm.pull_out_files')
    @patch('itolapi.Comm.requests')
    def test_export_image(self, mock_requests, mock_pull):
        mock_pull.return_value = (self.params, self.files)
        mock_requests.post().content = 'asdf'
        output = self.comm.export_image(self.params)
        self.assertEqual(output, 'asdf')
