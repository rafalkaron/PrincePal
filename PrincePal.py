# coding: UTF-8
"""
Preview your PDFs like a prince!
"""

import webbrowser
import sys
import os
import glob
from multiprocessing import Pool
import argparse
import send2trash

__version__ = "0.3"
__author__ = "Rafał Karoń <rafalkaron@gmail.com>"

def exe_dir():
    """Return the executable directory."""
    if getattr(sys, 'frozen', False):
        exe_path = os.path.dirname(sys.executable)
        #exe_path = os.path.dirname(os.path.dirname(os.path.dirname(exe_pat))) # Uncomment for macOS app builds
    elif __file__:
        exe_path = os.path.dirname(__file__)
    return exe_path

def files_list(directory, files_extension):
    """Return a list of files with a given extension in a directory."""
    if os.name == "nt":     # Windows ignores file extension case. Getting uppercase and lowercase lists generates duplicates.
        files_list = glob.glob(f"{directory}/*.{files_extension}")
    if os.name == "posix":  # macOS does not ignore file extension case.
        files_list_lowercase = glob.glob(f"{directory}/*.{files_extension.lower()}")
        files_list_uppercase = glob.glob(f"{directory}/*.{files_extension.upper()}")
        files_list = files_list_lowercase + files_list_uppercase
    return files_list

def publish_pdf(source_file):
    """Use the prince command to convert an HTML file to a PDF file and open the PDF file in the default application determined by OS."""    
    os.system(f"prince \"{source_file}\"")
    webbrowser.open(url=f"file:///{source_file.lower().replace('.html', '.pdf')}", new=1, autoraise=False)

def main():
    par = argparse.ArgumentParser(description="Preview your PDFs like a prince!")
    par.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    par.add_argument("-rm", "--remove_pdfs", action="store_true", help="moves PDF files from the script directory to trash")
    par.add_argument("-jobs", "--concurrent_jobs", metavar="jobs_number", help="determine the number of concurrent PDF generation jobs (defults to 12)")
    args = par.parse_args()
    # Consider creating an if = true loop listening to any saves in the script directory/children directories. run script on save
    # Add a functionality to remove PDFs from the directory.

    if not args.remove_pdfs:
        source_files = files_list(exe_dir(), "html")
        p = Pool(12)
        p.map(publish_pdf, source_files)
        p.close()
        p.join()

    if args.remove_pdfs:
        pdfs = files_list(exe_dir(), "pdf")
        for pdf in pdfs:
            send2trash.send2trash(pdf)

__main__ = os.path.basename(os.path.abspath(sys.argv[0])).replace(".py","")
if __name__ == "__main__":
    main()