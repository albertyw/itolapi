import tempfile
import unittest

from itolapi import Comm


class CommTest(unittest.TestCase):
    def test_pull_out_files(self):
        params = {}
        params['asdf'] = 'qwer'
        params['zxcv'] = tempfile.TemporaryFile()
        new_params, files = Comm.Comm.pull_out_files(params)
        self.assertEqual(new_params, {'asdf': 'qwer'})
        self.assertEqual(files, {'zxcv': params['zxcv']})
