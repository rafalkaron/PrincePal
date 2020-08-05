# coding: UTF-8
"""
Preview your PDFs like a prince!
"""

import webbrowser
import sys
import os
import glob
import multiprocessing
import argparse
import time

__version__ = "0.5"
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

def commands_list(f_list=[], output="", style=""):
    command_list = []
    for file in f_list:
        command_list.append(f"prince \"{file}\" {output} {style}")
    return command_list

def publish_pdf(command):
    """Use the prince command to convert an HTML file to a PDF file and open the PDF file in the default application determined by OS."""        
    os.system(command)

def preview_pdf(source_file):
    webbrowser.open(url=f"file:///{source_file.lower().replace('.html', '.pdf')}", new=1, autoraise=False)

def main():
    #sys.tracebacklimit = 0 # Disables traceback messages
    par = argparse.ArgumentParser(description="Preview your PDFs like a prince!")
    par.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    par.add_argument("-rm", "--remove_pdfs", action="store_true", help="USE WITH CAUTION: Permanently remove PDF files from the script directory")
    par.add_argument("-nopr", "--no_preview", action="store_true", help="prevent PDFs from opening after publication")
    par.add_argument("-yolo", "--you_live_only_once", action="store_true", help="combine with the '-rm' argument to permanently remove the PDF files from the script directory without confirmation.")
    par.add_argument("-jobs", "--concurrent_jobs", metavar="jobs", help="determine the number of concurrent jobs (defults to 12)")
    par.add_argument("-cwd", "--current_working_directory", action="store_true", help="Use HTML files in the script directory as an input")
    par.add_argument("-i", "--input", metavar="source", help="Pick a source file or source folder on your own")
    par.add_argument("-o", "--output", metavar="store_true", help="Pick the output folder on your own")
    par.add_argument("-s", "--style", metavar="store_true", help="Pick the output folder on your own")
    args = par.parse_args()
    # Consider creating an if = true loop listening to any saves in the script directory/children directories. run script on save.
    # Add an exception that will terminate the script if no prince installation is found.
    # Consider adding custom input/output folder options
    # Consider adding an option to close every web browser tab
    
    # Concurrent jobs settings
    if not args.concurrent_jobs:
        """The default number of concurrent jobs."""
        p = multiprocessing.Pool(12)
    elif args.concurrent_jobs:
        """Custom number of concurrent jobs."""
        jobs = int(args.concurrent_jobs)
        p = multiprocessing.Pool(jobs)

    # Remove PDFs feature
    if args.remove_pdfs:
        """USE WITH CAUTION: Permanently remove PDF files from the script directory."""
        pdfs = files_list(exe_dir(), "pdf")
        pdfs_bullet_list = "\n * ".join([str(x) for x in pdfs])
        if not args.you_live_only_once:
            if len(pdfs) == 0:
                raise Exception(f"No PDFs in {exe_dir()} to remove. Exiting...")
            prompt = input(f"Do you want to PERMANENTLY REMOVE the following files:\n * {pdfs_bullet_list}\nEnter [Y/N]: ").lower()
            if prompt == "y":
                p.map(os.remove, pdfs)
                p.close()
                p.join()
                print("Removed the PDFs.")
            else:
                print("Keeping your PDFs intact and exiting...")
                sys.exit(0)
        else:
            if len(pdfs) == 0:
                raise Exception(f"No PDFs in {exe_dir()} to remove. Exiting...")
            p.map(os.remove, pdfs)
            p.close()
            p.join()
        sys.exit(0)

    # Publishing
    """Publish and open PDFs."""
    start_time = time.time()
    
    if args.output:
        command_output = f" -o \"{args.output}\""
    elif not args.output:
        command_output = ""
    if args.style:
        command_style = f" -s \"{args.style}\""
    elif not args.style:
        command_style = ""

    if args.current_working_directory:
        os.chdir(exe_dir())
        source_files = files_list(exe_dir(), "html")
        p.map(publish_pdf, commands_list(source_files, command_output, command_style))
    
    if args.input:
        if os.path.isdir(args.input):
            source_files = files_list(args.input, "html")
            p.map(publish_pdf, commands_list(source_files, command_output, command_style))
        elif os.path.isfile(args.input):
            source_files = args.input
            publish_pdf(f"prince \"{args.input}\" {command_output} {command_style}")
    
    elapsed_time = time.time() - start_time
    #print(f"Converted {len(source)} HTML file(s) to PDFs in {round(elapsed_time, 3)} seconds.")
    if not args.no_preview:
        if args.current_working_directory:
            p.map(preview_pdf, source_files)
        elif args.input and os.path.isfile(args.input):
            preview_pdf(source_files)
        elif args.input and os.path.dirname(args.input):
            p.map(preview_pdf, source_files)

    p.close()
    p.join()

"""
    if args.current_working_directory:
        source = files_list(exe_dir(), "html")
        p.map(publish_pdf, source)
        if not args.no_preview:
            p.map(preview_pdf, source)

    elif args.input:
        if os.path.isdir(args.input):
            source = files_list(args.input, "html")
            p.map(publish_pdf, source)
            if not args.no_preview:
                p.map(preview_pdf, source)

        elif os.path.isfile(args.input):
            source = args.input
            publish_pdf(source)
            if not args.no_preview:
                preview_pdf(source)
"""
    #if len(source) == 0:
    #    raise Exception(f"No HTML files to convert in {exe_dir()}\nMove PrincePal to the directory with HTML files that you want to convert.")
    


__main__ = os.path.basename(os.path.abspath(sys.argv[0])).replace(".py","") # The "__main__" name must be used in the if statement below because of multiprocessing.
if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()