"""
This is the main file for exporting of trees created by iTOL
See the README.txt for details
"""
import Comm
import sys

class ItolExport:
    """
    Instantiate the itolexport class with empty params and empty server
    """
    def __init__(self):
        """
        Instantiate class
        """
        self.params = dict({})
        self.comm = Comm.Comm()
    
    ###Setting Export Parameters
    def add_export_param_dict(self, param_dict):
        """
        Add a dictionary of parameters to the parameters to be used when exporting
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
    
    ###Do Exporting
    def export(self, export_location):
        """
        Call the export process
        Calling this directly assumes that the export filetype is already set in the export params
        @param filelocation: the location to write the export to
        @return: whether the export works
        """
        output = self.comm.export_image(self.params)
        file_handle = open(export_location,'w')
        file_handle.write(output)
        file_handle.close()


# Print help info to the command line
def print_help():
    """
    This prints some help info to the command line
    """
    print 'Usage: python itolexport.py TREEID FILELOCATION FORMAT [-r] [-d]'
    print '  or:  python itolexport.py -h'
    print 'TREEID is the itol id of the tree you would like to export'
    print 'FILELOCATION is where you would like the exported tree to be \
    saved to (any file at FILELOCATION will be OVERWRITTEN)'
    print 'FORMAT is the format/file type of the export; accepted values are: \
    png, svg, eps, ps, pdf, nexus, newick'
    print 'Calling itolexport.py will write the exported tree to filelocation'
    print ''
    print '  -h   Display this help message'
    print '  -r   Verbose Output'
    print '  -d   Display Datasets' 
    print ''
    print 'Use itol.py to upload trees using python to the iTOL website'
    print 'Read the README and itolexport.py source code for information about \
    more powerful iTOL exporting.'
    print ''
    print 'Report bugs to <albertyw@mit.edu>'

# Run from command line
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print 'Use -h for help'
        sys.exit(0)
    arg_1 = sys.argv[1]
    #Help argument
    if arg_1 == '--help' or arg_1 == '-h':
        print_help()
        sys.exit(0)
    #Single argument (not enough)
    if len(sys.argv) == 2 or len(sys.argv) == 3:
        print 'Use -h for help'
        sys.exit(0)
    
    #Check Verbosity and viewDatasets
    verbose = False
    view_datasets = False
    if '-r' in sys.argv:
        verbose = True
    if '-d' in sys.argv:
        view_datasets = True
    
    #Three expected arguments
    tree_id = sys.argv[1]
    file_location = sys.argv[2]
    tree_format = sys.argv[3]
    itol_exporter = ItolExport()
    itol_exporter.set_export_param_value('tree', tree_id)
    itol_exporter.set_export_param_value('format', tree_format)
    if view_datasets == True:
        itol_exporter.set_export_param_value('datasetList', \
            'dataset1,dataset2,dataset3,dataset4,dataset5,\
            dataset6,dataset7,dataset8,dataset9,dataset10')
    print 'Exporting tree from server....'
    itol_exporter.export(file_location)
    print 'Exported to ', file_location
    sys.exit(0)
