"""
This is the main file for the iTOL API
"""
from __future__ import unicode_literals

import argparse
import os

from six import string_types

from itolapi import Comm, ItolExport


class Itol:
    """
    This class handles the main itol functionality
    """

    def __init__(self):
        """
        Initialize a few required variables
        """
        self.variables = dict()
        self.comm = Comm.Comm()

    def add_variable(self, variable_name, variable_value):
        """
        Add a variable and its value to this upload.  This function includes
        some basic variable checking and should be used instead of directly
        modifying the variables dictionary
        """
        # Variable checking
        if not isinstance(variable_name, string_types):
            raise TypeError('variable name is not a string')
        if not isinstance(variable_value, string_types):
            raise TypeError('variable value should be a string')
        if self.is_file(variable_name):
            if not os.path.isfile(variable_value):
                raise IOError('variable name ' + variable_name +
                              ' indicates value should be a file')
            variable_value = open(variable_value, 'r')
        # Add the variable
        self.variables[variable_name] = variable_value
        return True

    @staticmethod
    def is_file(variable_name):
        """
        This returns a boolean whether the string in variable_name is a file
        This is determined by looking at whether "File" is a substring of
        variable_name; this assumes that variable_name is a string
        """
        if variable_name.find('File') != -1:
            return True
        else:
            return False

    def upload(self):
        """
        Upload the variables to the iTOL server and return an ItolExport object
        """
        good_upload = self.comm.upload_tree(self.variables)
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
        itol_exporter = ItolExport.ItolExport()
        itol_exporter.set_export_param_value('tree', self.comm.tree_id)
        return itol_exporter

    def print_variables(self):
        """
        Print the variables that have been set so far
        """
        for variable_name, variable_value in self.variables.items():
            if hasattr(variable_value, 'name'):
                print(variable_name + ': ' + variable_value.name)
            else:
                print(variable_name + ': ' + variable_value)

    def delete_variable(self, variable_name):
        """
        Remove a variable from the dictionary of set variables
        """
        if variable_name in self.variables:
            del self.variables[variable_name]


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
    itol_upload.add_variable('treeFile', tree_file)
    itol_upload.upload()
    print(itol_upload.get_webpage())
