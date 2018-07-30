import os
import tempfile
import unittest

from itolapi import Itol


class TestIntegration(unittest.TestCase):
    def test_upload_download(self):
        current_dir = os.path.dirname(os.path.realpath(__file__))
        examples_dir = os.path.join(current_dir, '..', '..', 'examples')

        test = Itol()
        tree = os.path.join(examples_dir, 'tree_of_life.tree.txt')
        test.add_file(tree)
        dataset = os.path.join(examples_dir, 'colors_tol.txt')
        test.add_file(dataset)
        upload_status = test.upload()

        self.assertTrue(upload_status)

        exporter = test.get_itol_export()
        exporter.set_export_param_value('format', 'pdf')
        with tempfile.NamedTemporaryFile() as temp:
            exporter.export(temp.name)
