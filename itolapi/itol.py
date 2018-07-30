"""
This is the main file for the iTOL API
"""
from __future__ import unicode_literals

import argparse
import os
import pprint

from itolapi import Comm, ItolExport


class Itol:
    """
    This class handles the main itol functionality
    """

    def __init__(self):
        """
        Initialize a few required variables
        See http://itol.embl.de/help.cgi#bUpOpt for available params
        """
        self.files = []
        self.params = {
            'uploadID': '',
            'projectName': '',
            'treeName': '',
            'treeDescription': '',
        }
        self.comm = Comm()

    def add_file(self, file_path):
        """
        Add a file to be uploaded, tree or dataset
        """
        if not os.path.isfile(file_path):
            raise IOError('%s is not a file' % file_path)
        self.files.append(file_path)

    def upload(self):
        """
        Upload the data to the iTOL server and return an ItolExport object
        """
        good_upload = self.comm.upload_tree(self.files, self.params)
        if good_upload:
            return self.comm.tree_id
        else:
            self.comm.tree_id = 0
            return False

    def get_webpage(self):
        """
        Get the web page where you can download the Itol tree
        """
        webpage = "http://itol.embl.de/external.cgi?tree=" +\
            str(self.comm.tree_id) + "&restore_saved=1"
        return webpage

    def get_itol_export(self):
        """
        Returns an instance of ItolExport in preparation of exporting from the
        generated tree
        @return: instance of ItolExport
        """
        itol_exporter = ItolExport()
        itol_exporter.set_export_param_value('tree', self.comm.tree_id)
        return itol_exporter

    def print_variables(self):
        """
        Print the files and params that have been set so far
        """
        print('Files:')
        pprint.pprint(self.files)
        print('Parameters:')
        pprint.pprint(self.params)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="iTOL Uploader",
        epilog="Report bugs at https://github.com/albertyw/itolapi/"
    )
    parser.add_argument(
        'tree_file', help="path to the tree file to be uploaded to iTOL")
    args = parser.parse_args()
    tree_file = args.tree_file

    itol_upload = Itol()
    itol_upload.add_file(tree_file)
    itol_upload.upload()
    print(itol_upload.get_webpage())
