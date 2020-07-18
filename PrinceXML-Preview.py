# coding: UTF-8
"""
Preview your PDFs like a Prince!

Do the following:
* Install Prince XML on your machine.
* Create a HTML file and a CSS file in a single directory.
* Put this script in the HTML file and CSS file directory.
* Run this script.

Results:
* Prince renders every HTML file in the script directory to a PDF.
* Every PDF is opened in the default application that opens PDFs in your OS.
Note: I recommend setting your default PDF application to a web browser like Chrome or Brave - this way, each way you run this script, a new tab opens and you can quickly compare your CSS edits.
"""

import webbrowser
import sys
import os
import glob

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
    """Use Prince XML to publish a PDF from HTML"""    
    os.system(f"prince {source_files}")

def files_list(directory, files_extension):
    """Return a list of files with a given extension in a directory."""
    files_list = glob.glob(f"{directory}/*.{files_extension.lower()}")
    return files_list

def preview(output_file):
    """Open the published PDF in a default application - I suggest using Chrome/Brave"""
    webbrowser.open(url=f"file:///{output_file}", new=1, autoraise=False)

def main():
    # Consider implementing multithreading
    # Consider creating an if = true loop listening to any saves in the script directory/children directories. run script on save
    for source_file in files_list(exe_dir(), "html"):
        publish_pdf(source_file)
    
    for output_file in files_list(exe_dir(), "pdf"):
        preview(output_file)
main()