"""
This is the main file for exporting of trees created by iTOL
"""
from __future__ import unicode_literals

import argparse
import sys

from itolapi import Comm


class ItolExport:
    EXPORT_FORMATS = ['png', 'svg', 'eps', 'ps', 'pdf', 'nexus', 'newick']
    """
    Instantiate the itolexport class with empty params and empty server
    """

    def __init__(self):
        """
        Instantiate class
        """
        self.params = dict({})
        self.comm = Comm.Comm()

    # Setting Export Parameters
    def add_export_param_dict(self, param_dict):
        """
        Add a dictionary of parameters to the parameters to be used when
        exporting
        @param: dictionary of parameters to be used
        """
        self.params.update(param_dict)

    def set_export_param_value(self, key, value):
        """
        Add a value to the dictionary of parameters to be used when exporting
        @param: dictionary of parameters to be used
        """
        self.params[key] = value

    def get_export_params(self):
        """
        Get the dictionary of parameters to tbe used when exporting
        @return: export the Parameters
        """
        return self.params

    # Do Exporting
    def export(self, export_location):
        """
        Call the export process
        Calling this directly assumes that the export filetype is already set
        in the export params
        @param filelocation: the location to write the export to
        @return: whether the export works
        """
        output = self.comm.export_image(self.params)
        file_handle = open(export_location, 'wb')
        file_handle.write(output)
        file_handle.close()


# Run from command line
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="iTOL Downloader",
        epilog="Report bugs at https://github.com/albertyw/itolapi/"
    )
    parser.add_argument(
        'tree_id', help="iTOL ID of the tree you are exporting", type=int)
    parser.add_argument(
        'file_location', help="File path to write exported tree to")
    parser.add_argument('format', help="Exported data format",
                        choices=ItolExport.EXPORT_FORMATS)
    parser.add_argument('-d', '--dataset', help="Show datasets")
    parser.add_argument('-v', '--verbose', help='Verbose')
    args = parser.parse_args()

    itol_exporter = ItolExport()
    itol_exporter.set_export_param_value('tree', str(args.tree_id))
    itol_exporter.set_export_param_value('format', args.format)
    if args.dataset:
        itol_exporter.set_export_param_value('datasetList',
                                             'dataset1,dataset2,dataset3,dataset4,dataset5,\
            dataset6,dataset7,dataset8,dataset9,dataset10')
    print('Exporting tree from server....')
    itol_exporter.export(args.file_location)
    print('Exported to ', args.file_location)
    sys.exit(0)
