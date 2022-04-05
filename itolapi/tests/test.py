import os
from pathlib import Path
import tempfile
import unittest

from itolapi import Itol


class TestIntegration(unittest.TestCase):
    @unittest.skip("No API subscription")
    def test_upload_download(self) -> None:
        current_dir = Path(os.path.realpath(__file__)).parent
        examples_dir = current_dir.parent.parent / 'examples'

        test = Itol()
        tree = examples_dir / 'tree_of_life.tree.txt'
        test.add_file(tree)
        dataset = examples_dir / 'colors_tol.txt'
        test.add_file(dataset)
        upload_status = test.upload()

        self.assertTrue(upload_status)

        exporter = test.get_itol_export()
        exporter.set_export_param_value('format', 'pdf')
        with tempfile.NamedTemporaryFile() as temp:
            exporter.export(Path(temp.name))
