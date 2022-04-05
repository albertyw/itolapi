'''
This is an example script for using itol.py
To use itol.py, you essentially have to instantiate the object, set the tree,
submit the file to itol, then use the returned data
'''

import os
from pathlib import Path
import sys

current_dir = Path(os.path.realpath(__file__)).parent
root_path = current_dir.parent
sys.path.append(str(root_path))

from itolapi import Itol, ItolExport  # NOQA

print('Running example itol and itolexport script')
print('')
print('Creating the upload params')

# Create the Itol class
test = Itol()

# Set the tree file
tree = current_dir / 'tree_of_life.tree.txt'
test.add_file(tree)
test.add_file(current_dir / 'colors_tol.txt')
test.add_file(current_dir / 'labels.txt')
test.add_file(current_dir / 'ranges.txt')
# Add parameters
test.params['treeName'] = 'Tree of Life Example'
# Check parameters
test.print_variables()
# Submit the tree
print('')
print((
    'Uploading the tree.  This may take some time depending on how large the '
    'tree is and how much load there is on the itol server'
))
good_upload = test.upload()
if not good_upload:
    print('There was an error:' + test.comm.upload_output)
    sys.exit(1)

# Read the tree ID
print('Tree ID: ' + test.comm.tree_id)

# Read the iTOL API return statement
print('iTOL output: ' + test.comm.upload_output)

# Website to be redirected to iTOL tree
print('Tree Web Page URL: ' + test.get_webpage())

# Warnings associated with the upload
print('Warnings: ', test.comm.warnings)


# Export a pre-made tree to pdf
itol_exporter = ItolExport()
itol_exporter.set_export_param_value('tree', '18793532031912684633930')
itol_exporter.set_export_param_value('format', 'pdf')
itol_exporter.set_export_param_value('datasetList', 'dataset1')
# itol_exporter.export('example_pdf.pdf')
# print('exported tree to ',export_location)

# Export the tree above to pdf
print('Exporting to pdf')
itol_exporter = test.get_itol_export()
export_location = current_dir / 'example_pdf.pdf'
itol_exporter.set_export_param_value('format', 'pdf')
itol_exporter.set_export_param_value('datasetList', 'dataset1')
itol_exporter.export(export_location)
print('exported tree to ', export_location)
