'''
This is an example script for using itol.py
To use itol.py, you essentially have to instantiate the object, set the tree, submit the file to itol, then use the returned data
'''

import os
import sys

pathname = os.path.dirname(sys.argv[0])
fullpath = os.path.abspath(pathname)
parent_path = fullpath + "/../"
sys.path.append(parent_path)

from itolapi import Itol, ItolExport

print('Running example itol and itolexport script')
print('')
print('Creating the upload params')

# Create the Itol class
test = Itol.Itol()

# Set the tree file
tree = fullpath + '/example_tree'
test.add_variable('treeFile', tree)
# Add parameters
test.add_variable('treeName', 'adsf')
test.add_variable('treeFormat', 'newick')
test.add_variable('dataset1File', fullpath + '/example_data')
test.add_variable('dataset1Label', 'colors')
test.add_variable('dataset1Separator', 'comma')
test.add_variable('dataset1Type', 'multibar')
# Check parameters
test.print_variables()
# Submit the tree
print('')
print('Uploading the tree.  This may take some time depending on how large the tree is and how much load there is on the itol server')
good_upload = test.upload()
if not good_upload:
    print('There was an error:' + test.comm.upload_output)
    sys.exit(1)

# Read the tree ID
print('Tree ID: ' + str(test.comm.tree_id))

# Read the iTOL API return statement
print('iTOL output: ' + str(test.comm.upload_output))

# Website to be redirected to iTOL tree
print('Tree Web Page URL: ' + test.get_webpage())

# Warnings associated with the upload
print('Warnings: ' + str(test.comm.warnings))


# Export a pre-made tree to pdf
itol_exporter = ItolExport.ItolExport()
itol_exporter.set_export_param_value('tree', '18793532031912684633930')
itol_exporter.set_export_param_value('format', 'pdf')
itol_exporter.set_export_param_value('datasetList', 'dataset1')
# itol_exporter.export('example_pdf.pdf')
#print('exported tree to ',export_location)

# Export the tree above to pdf
print('Exporting to pdf')
itol_exporter = test.get_itol_export()
export_location = 'example_pdf.pdf'
itol_exporter.set_export_param_value('format', 'pdf')
itol_exporter.set_export_param_value('datasetList', 'dataset1')
itol_exporter.export('example_pdf.pdf')
print('exported tree to ', export_location)
