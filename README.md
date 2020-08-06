# PrincePal
*Preview your PDFs like a prince!*

**Before you begin:**
* Download the latest **PrincePal** version. See [PrincePal Download](https://github.com/rafalkaron/PrincePal/releases/latest)  
**NOTE:** You can download a Windows bundle, macOS bundle, or a non-compiled Python script.
* If you want to run non-compiled **PrincePal**, install **Python 3.8.2** or higher. See [Properly Installing Python](https://docs.python-guide.org/starting/installation/).
* Install **Prince**. See [Prince - Getting Started](https://www.princexml.com/doc/installing/).
* Begin developing a Prince PDF style. See [Your First Document](https://www.princexml.com/doc/first-doc/).  
**TIP:** Ensure that the HTML files do not contain any broken references because they significantly slow down conversion.

**Procedure:**
**NOTE:** You may need to run **PrincePal** as an administrator.  
Every PDF file opens in the default application determined by your OS settings. I recommend setting a web browser (e.g. Chrome or Brave) to open PDFs by default in your OS settings. This way, each time you run **PrincePal**, a new tab opens so you can quickly compare your styling modifications.

Do any of the following: 
* To convert the HTML files in the **PrincePal** directory:
    * Put **PrincePal** in the HTML files directory.
    * Run **PrincePal** with the *-cwd* attribute.
* To convert the HTML files in a given directory, run **PrincePal** with the *-i* attribute followed by the directory path.
* To convert a single HTML file, run **PrincePal** with the *-i* attribute followed by the file path.
* If needed, accept any security prompts. See [Accepting macOS Security Prompts](https://github.com/rafalkaron/PrincePal/wiki/Accepting-macOS-Security-Prompts) or [Accepting Windows Security Prompts](https://github.com/rafalkaron/PrincePal/wiki/Accepting-Windows-Security-Prompts).

Optional arguments:
* To use a CSS style, use the *-s* attribute followed by the file path to the CSS file.
* To prevent the PDF preview from opening use the *-nopr* attribute.
* To set the number of concurrent jobs, use the *-jobs* attribute.  
**NOTE:** The number of concurrent conversion, removal, and preview jobs defaults to 12. You can use this attribute with other attributes.