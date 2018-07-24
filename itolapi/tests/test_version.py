import unittest

from itolapi import __version__


class TestVersion(unittest.TestCase):
    def test_version(self):
        self.assertTrue(__version__.__version__)
        self.assertTrue(__version__.VERSION)
