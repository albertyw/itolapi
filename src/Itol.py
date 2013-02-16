"""
This is the main file for the iTOL API
See the README.txt for details
"""
import sys
import os
import Comm
import ItolExport

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
        if not isinstance(variable_name, str):
            raise TypeError('variable name is not a string')
        if not isinstance(variable_value, str):
            raise TypeError('variable value should be a string')
        if self.is_file(variable_name):
            if not os.path.isfile(variable_value):
                raise IOError('variable name '+variable_name+\
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
        if variable_name.find('File')!=-1:
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
        webpage = "http://itol.embl.de/external.cgi?tree="+\
            str(self.comm.tree_id)+"&restore_saved=1"
        return webpage
    
    def get_itol_export(self):
        """
        Returns an instance of ItolExport in preparation of exporting from the generated tree
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
            if isinstance(variable_value, file):
                print variable_name+': '+variable_value.name
            else:
                print variable_name+': '+variable_value
        
    def delete_variable(self, variable_name):
        """
        Remove a variable from the dictionary of set variables
        """
        if self.variables.has_key(variable_name):
            del self.variables[variable_name]
        
        
def print_help():
    """
    This just prints help information for people calling this script 
    from console
    """
    print 'Usage: python itol.py TREEFILE'
    print '  or:  python itol.py -h'
    print 'TREEFILE is the path to the tree file to be uploaded to iTOL'
    print 'Calling Itol.py with an acceptable tree file \
    will return a URL to access the tree'
    print ''
    print '  -h    Display this help message'
    print ''
    print 'Use ItolExport.py to export uploaded trees from iTOL'
    print 'Read the README.txt and Itol.py source code for \
    information about more powerful iTOL calls.'
    print ''
    print 'Report bugs to <albertyw@mit.edu>'

    
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print_help()
        sys.exit()
    if sys.argv[1] == '-h':
        print_help()
        sys.exit()
    try:
        itol_upload = Itol()
        itol_upload.add_variable('treeFile', sys.argv[1])
        itol_upload.upload()
        print itol_upload.get_webpage()
    except:
        print_help()
