from pathlib import Path
import tempfile
import unittest
from unittest.mock import MagicMock, patch

from itolapi import Itol


class ItolTest(unittest.TestCase):

    def setUp(self) -> None:
        self.itol = Itol()

    def test_initializes(self) -> None:
        self.assertEqual(type(self.itol.params), dict)
        self.assertEqual(self.itol.files, [])
        self.assertIsNotNone(self.itol.comm)

    def test_add_file(self) -> None:
        with tempfile.NamedTemporaryFile() as temp:
            self.itol.add_file(Path(temp.name))
        with self.assertRaises(IOError):
            self.itol.add_file(Path('/asdf'))

    def test_good_upload(self) -> None:
        with patch('itolapi.Comm.upload_tree') as mock_upload:
            mock_upload.return_value = True
            self.itol.comm.tree_id = '1234'
            self.assertEqual(self.itol.upload(), '1234')

    def test_bad_upload(self) -> None:
        with patch('itolapi.Comm.upload_tree') as mock_upload:
            mock_upload.return_value = False
            self.itol.comm.tree_id = '1234'
            self.assertEqual(self.itol.upload(), 0)

    def test_get_webpage(self) -> None:
        self.itol.comm.tree_id = 'asdf'
        webpage = self.itol.get_webpage()
        self.assertIn('itol.embl.de', webpage)
        self.assertIn('asdf', webpage)

    def test_get_itol_export(self) -> None:
        self.itol.comm.tree_id = '1234'
        export = self.itol.get_itol_export()
        self.assertEqual(export.params['tree'], '1234')

    @patch('itolapi.itol.pprint.pprint')
    def test_print_variables(self, mock_print: MagicMock) -> None:
        self.itol.params['treeName'] = 'test'
        with tempfile.NamedTemporaryFile() as temp:
            self.itol.add_file(Path(temp.name))
            self.itol.print_variables()
        self.assertEqual(mock_print.call_args_list[0][0][0], self.itol.files)
        self.assertEqual(mock_print.call_args_list[1][0][0], self.itol.params)
