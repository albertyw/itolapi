"""
This file tests basic uploading with a treeFile, colorDefinitionFile, and a
data1File.  It also includes some non-fatal warnings.
"""

import os
import sys

pathname = os.path.dirname(sys.argv[0])
fullpath = os.path.abspath(pathname)
parent_path = fullpath + "/../../"
sys.path.append(parent_path)

from itolapi import Itol  # NOQA

parse_fn = 'huge.matrix.tree.parse'
color_fn = 'huge.matrix.tree.parse.color'
abun_fn = 'huge.matrix.tree.parse.abun'

itol_o = Itol.Itol()
itol_o.add_variable('treeFile', parse_fn)
itol_o.add_variable('treeName', 'HuGE Tree')
itol_o.add_variable('treeFormat', 'newick')
itol_o.add_variable('colorDefinitionFile', color_fn)
itol_o.add_variable('dataset1File', abun_fn)
itol_o.add_variable('dataset1Label', 'Abundance')
itol_o.add_variable('dataset1Separator', 'comma')
itol_o.add_variable('dataset1Type', 'multibar')
itol_o.add_variable('dataset1Color', '#ff0000')
itol_o.add_variable('dataset1MultiBarAlign', '1')
itol_o.add_variable('dataset1PieTransparent', '0')
itol_o.add_variable('dataset1PieRadiusMax', '100')
itol_o.add_variable('dataset1PieRadiusMin', '20')
itol_o.add_variable('dataset1BarSizeMax', '20')
itol_o.print_variables()
good_upload = itol_o.upload()
print('Tree Web Page URL:\n' + itol_o.get_webpage() + '\n')
print('Warnings:')
print(itol_o.comm.warnings)
