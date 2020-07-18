# coding: UTF-8
"""
Preview your PDFs like a prince!
"""

import webbrowser
import sys
import os
import glob
from multiprocessing import Pool
import re

__version__ = "0.1"
__author__ = "Rafał Karoń <rafalkaron@gmail.com>"

def exe_dir():
    """Return the executable directory."""
    if getattr(sys, 'frozen', False):
        exe_path = os.path.dirname(sys.executable)
        #exe_path = os.path.dirname(os.path.dirname(os.path.dirname(exe_pat))) # Uncomment for macOS app builds
    elif __file__:
        exe_path = os.path.dirname(__file__)
    return exe_path
    
def publish_pdf(source_files):
    """Use the prince command to convert an HTML file to a PDF file."""    
    os.system(f"prince {source_files}")

def files_list(directory, files_extension):
    """Return a list of files with a given extension in a directory."""
    files_list_lowercase = glob.glob(f"{directory}/*.{files_extension.lower()}")
    files_list_uppercase = glob.glob(f"{directory}/*.{files_extension.upper()}")
    files_list = files_list_lowercase + files_list_uppercase
    return files_list

def preview(output_file):
    """Open the converted PDF file in the default application determined by your OS."""
    webbrowser.open(url=f"file:///{output_file}", new=1, autoraise=False)

def main():
    # Consider creating an if = true loop listening to any saves in the script directory/children directories. run script on save

    # Singleprocessing - works bot with Python 3.8.2 and Python 3.7.3
    """
    for source_file in files_list(exe_dir(), "html"):
        publish_pdf(source_file)
        preview(source_file.lower().replace(".html", ".pdf"))
    """

    # Multiprocessing - does not work with Python 3.8.2. Works correctly with 3.7.3
    p = Pool()
    source_files = files_list(exe_dir(), "html")
    p.map(publish_pdf, source_files)
    #p.map(preview, files_list(exe_dir(), "pdf")) # This opens new tabs for every PDF in the current folder now.
    for output_file in source_files:
        preview(output_file.lower().replace(".html", ".pdf"))
    p.close()
    p.join()

main()