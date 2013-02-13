ITOL-API
========

Python API for the Interactive Tree of Life (iTOL)

Created by Albert Wang (albertyw@mit.edu), Updated March 2011

With Complements to: [iTOL (Interactive Tree of Life)](http://itol.embl.de/), [urllib2_file by Fabien Seisen](https://github.com/seisen/urllib2_file)

This iTOL API is meant to link between local programs written in Python and the iTOL website.  Itol.py can be used to upload trees and datasets from a Python program or command line onto iTOL for processing and viewing.  ItolExport.py can export (download) trees from iTOL to the local computer for viewing.  An active internet connection to the [iTOL website](http://itol.embl.de/) is required.
  
Files Required:  
Itol.py: Overall handling of parameters, datasets, tree file, processing of trees through calls to dataset.py, itolFile.py, server.py, urllib2_file.py  
ItolExport.py: Overall handling of parameters for exporting/downloading tree visualizations from itol  
Comm.py: Handles communication to itol website and stores returned data  
urllib2\_file.py: Helps itol.py upload tree files  

UPLOADING TREES TO ITOL (ITOL.PY)
----------------------------------------------------------------
###RUNNING FROM COMMAND LINE
(If you need to do anything more than displaying basic tree structures, you must call the Python iTOL API from within a Python program)  

To run Python from the command line, a newick tree must be saved to a file that can be accessed by the itol.py script.  To upload the newick tree to iTOL for processing, run itol.py with the script location as the first argument.  The output of the script should be a url that at http://itol.embl.de/ that can be used to access the drawn tree

####Examples:

"python /path/to/Itol.py /path/to/example.tree"

####Example Output For A Good File:

"http://itol.embl.de/external.cgi?tree=18793532558412678134820&restore\_saved=1"


###RUNNING FROM A PYTHON PROGRAM

Running from a python program is much more flexible than running from command line and allows access to all options found at [http://itol.embl.de/help/batch_help.shtml](http://itol.embl.de/help/batch_help.shtml)

The steps to run the iTOL Python API are:

1.  Import the iToL API  
Assuming that the itol api files are in the Python path, type "import Itol" in order to be able to call the iTOL Python API

2.  Instantiate iToL  
Create a variable (e.g. "itol\_uploader") and set it to an instance of itol.py (e.g. "itol\_uploader = Itol.Itol()")

3.  Set the Tree  
To set the tree, use "itol\_uploader.add\_variable('treeFile','/path/to/file')" 

4.  Set Any Additional Parameters (Optional)  
To set parameters one by one, call "itol\_uploader.add_variable(var\_name, var\_value)" as many times as needed
Dataset variables can also be set with dataset# prefixing the variable name using add\_variable()
The list of accepted variable names and allowed values is found at http://itol.embl.de/help/batch\_help.shtml.  

5.  Upload the tree  
Call itol_uploader.upload()  
The returned value will be False if iTOL got an error, or the tree id if the upload was good

6.  Get the iTOL output:  
If the returned value of the previous step was True,  
Call "itol\_uploader.comm.upload\_output" to get the raw return statement of iTOL AND/OR  
Call "itol\_uploader.comm.tree\_id" to get the tree ID (string) created by iTOL for your upload AND/OR  
Call "itol\_uploader.get\_webpage()" to get the web page url at the iTOL website to view the uploaded tree AND/OR  
Call "itol\_uploader.get_itol\_export()" to get an instance of ItolExport in order to download your uploaded tree in different formats

An example for using the Python iTOL API can found in example.py

##DOWNLOADING TREES FROM ITOL (ITOLEXPORT.PY)##
###RUNNING FROM COMMAND LINE
(If you would like to set any parameters other than the tree id, 
location to save the file, file format, and whether to display datasets, 
you must use itolexport from a Python program)

To export pre-uploaded itol files, call "python ItolExport.py TREEID FILELOCATION FORMAT" where  
TREEID is the itol id where the tree was uploaded,  
FILELOCATION is the location to save the exported tree, and  
FORMAT is the type of export you would like to perform.  
You can add a -r flag for verbose output and -d to also show datasets.  Call "python itolexport.py -h" for help.  

###RUNNING FROM A PYTHON PROGRAM
Running itolexport.py from a Python program allows you to use all the options that iTOL has available.  
The steps to run itolexport from a Python program are:

1.  Import  
Assuming that the itol API programs are in your Python path, type "import ItolExport"

2.  Instantiate  
Call "itol\_exporter = ItolExport.ItolExport()"

3.  Select a tree ID to export  
Call "itol\_exporter.add\_export\_param\_value('tree',tree\_id)" where tree\_id is a string of the tree id on iTOL

4.  Add an output format  
Call "itol\_exporter.add\_export_param\_value('format',format)" where format represents the format to export.  
Allowed formats are png, svg, eps, ps, pdf, nexus, newick

5.  Add any other parameters (Optional)  
Call "itol\_exporter.add\_export\_param\_value(param\_key,param\_value)" where param\_key and param\_value are the name of a parameter name and value.  
The allowed paramKeys and their values can be found at http://itol.embl.de/help/batch\_help.shtml.

6.  Export  
Call "itol\_exporter.export(file\_location)" where file_location is the path to the location to write the export to.  
If a file is already in that location, it will be overwritten.  This step may take a while depending on how big of a tree you are exporting.  



Send e-mails to Albert Wang (the repo owner) for questions and comments