from mock import MagicMock, patch
import tempfile
import unittest

from itolapi import Comm


class PullOutFilesTest(unittest.TestCase):
    def test_pull_out_files(self):
        params = {}
        params['asdf'] = 'qwer'
        params['zxcv'] = tempfile.TemporaryFile()
        new_params, files = Comm.Comm.pull_out_files(params)
        self.assertEqual(new_params, {'asdf': 'qwer'})
        self.assertEqual(files, {'zxcv': params['zxcv']})

    def test_doesnt_modify_params(self):
        params = {}
        params['asdf'] = 'qwer'
        params['zxcv'] = tempfile.TemporaryFile()
        Comm.Comm.pull_out_files(params)
        self.assertTrue('asdf' in params)
        self.assertTrue('zxcv' in params)

class UploadTreeTest(unittest.TestCase):
    def setUp(self):
        self.comm = Comm.Comm()
        self.params = {'asdf': 'qwer'}
        self.files = {'zxcv': tempfile.TemporaryFile()}
        self.all_params = self.params.copy()
        self.all_params.update(self.files)

    @patch('itolapi.Comm.Comm.pull_out_files')
    @patch('itolapi.Comm.requests')
    @patch('itolapi.Comm.Comm.parse_upload')
    def test_upload_tree(self, mock_parse, mock_requests, mock_pull):
        mock_pull.return_value = (self.params, self.files)
        mock_requests.post().text = 'asdf'
        mock_parse.return_value = 'qwer'
        output = self.comm.upload_tree(self.all_params)
        mock_pull.assert_called_once_with(self.all_params)
        mock_requests.post.assert_called_with(self.comm.upload_url, data=self.params, files=self.files)
        mock_parse.assert_called_once()
        self.assertEqual(self.comm.upload_output, 'asdf')
        self.assertEqual(output, 'qwer')


