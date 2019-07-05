"""
This file is for communication between this API and iTOL servers
This also processes and stores information returned from the server
"""
from __future__ import unicode_literals
import os
import tempfile
import zipfile

import requests


class Comm:
    """
    This class handles communication between the API and the iTOL servers
    This also processes and stores information returned from the server
    """

    def __init__(self):
        """
        Initialize
        """
        self.upload_url = 'https://itol.embl.de/batch_uploader.cgi'
        self.export_url = 'https://itol.embl.de/batch_downloader.cgi'
        self.upload_output = ''
        self.export_output = ''
        self.tree_id = ''
        self.warnings = []

    @staticmethod
    def create_zip_from_files(files):
        """
        Write files into a zip file for uploading
        """
        temp = tempfile.NamedTemporaryFile()
        with zipfile.ZipFile(temp, 'w') as handle:
            for f in files:
                filename = os.path.basename(f)
                handle.write(f, arcname=filename)
        temp.flush()
        return temp

    def upload_tree(self, files, params):
        """
        Submit the File to Itol using api at self.upload_url;
        files is a list of file paths that will be zipped and uploaded
        params is the dictionary of variables that will be uploaded
        """
        temp_zip = Comm.create_zip_from_files(files)
        files = {'zipFile': open(temp_zip.name, 'rb')}
        response = requests.post(self.upload_url, data=params, files=files)
        files['zipFile'].close()
        temp_zip.close()
        data = response.text
        self.upload_output = data
        good_upload = self.parse_upload()
        return good_upload

    def parse_upload(self):
        """
        Parse the raw returned output for uploading to iTOL
        The output is read from self.upload_output
        @return: True if the tree is uploaded successfully or successfully
                 with warnings; False if error occured
        """
        if 'SUCCESS' not in self.upload_output:
            # Fatal Error
            self.warnings = [self.upload_output]
            return False
        self.warnings = self.upload_output.strip().split("\n")[0:-1]
        self.tree_id = self.upload_output.strip().split("\n")[-1].split()[1]
        return True

    def export_image(self, params):
        """
        Submit an export request to Itol using api at self.export_url
        @return: true if connection was established to server
        """
        response = requests.post(self.export_url, data=params)
        self.export_output = response.content
        return self.export_output
