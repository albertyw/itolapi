"""
This file is for communication between this API and iTOL servers
This also processes and stores information returned from the server
"""
from __future__ import unicode_literals

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
        self.upload_url = 'http://itol2.embl.de/batch_uploader.cgi'
        self.export_url = 'http://itol2.embl.de/batch_downloader.cgi'
        self.upload_output = ''
        self.export_output = ''
        self.tree_id = ''
        self.warnings = []

    @staticmethod
    def pull_out_files(params):
        """
        Pull out file objects so they can be fed into requests separately
        """
        new_params = {}
        files = {}
        for k, v in params.items():
            if hasattr(v, 'read'):
                files[k] = v
            else:
                new_params[k] = v
        return new_params, files

    def upload_tree(self, params):
        """
        Submit the File to Itol using api at self.upload_url
        params is the dictionary of variables that will be uploaded
        """
        params, files = Comm.pull_out_files(params)
        response = requests.post(self.upload_url, data=params, files=files)
        data = response.text
        self.upload_output = data
        good_upload = self.parse_upload()
        return good_upload

    def parse_upload(self):
        """
        Parse the raw returned output for uploading to iTOL
        The output is read from self.upload_output
        @return: True if the tree is uploaded successfully or successfully with warnings; False if error occured
        """
        if self.upload_output.find('SUCCESS') == -1:
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
        params, files = Comm.pull_out_files(params)
        response = requests.post(self.export_url, data=params, files=files)
        self.export_output = response.content
        return self.export_output
