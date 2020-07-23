# PrincePal
*Preview your PDFs like a prince!*

**Before you begin:**
* Download the latest **PrincePal** version. See [PrincePal Download](https://github.com/rafalkaron/PrincePal/releases/latest)  
**NOTE:** You can download a Windows bundle, macOS bundle, or a non-compiled Python script.
* If you want to run non-compiled **PrincePal**, install **Python 3.8.2** or higher. See [Properly Installing Python](https://docs.python-guide.org/starting/installation/).
* Install **Prince**. See [Prince - Getting Started](https://www.princexml.com/doc/installing/).
* Begin developing a Prince PDF style. See [Your First Document](https://www.princexml.com/doc/first-doc/).

**Procedure:**
1. Put **PrincePal** in the directory where you keep the HTML files that you want to convert to PDFs.  
**TIP:** Ensure that the HTML files do not contain any broken references because they significantly slow down conversion.
1. If needed, accept any security prompts. See [Accepting macOS Security Prompts](https://github.com/rafalkaron/PrincePal/wiki/Accepting-macOS-Security-Prompts) or [Accepting Windows Security Prompts](https://github.com/rafalkaron/PrincePal/wiki/Accepting-Windows-Security-Prompts).
2. Do one of the following:
    * To convert HTML files in the **PrincePal** directory to PDFs and open preview, run **PrincePal**.  
    **NOTE:** Every PDF file opens in the default application determined by your OS settings. I recommend setting a web browser (e.g. Chrome or Brave) to open PDFs by default in your OS settings. This way, each time you run **PrincePal**, a new tab opens so you can quickly compare your styling modifications.
    * To convert HTML files in the **PrincePal** directory to PDFs, run **PrincePal** with the *--no_preview* attribute.
    * **USE WITH CAUTION:** To remove every PDF file in the **PrincePal** directory, run **PrincePal** with the *--remove_pdfs* attribute.
    * To set the number of concurrent jobs, run **PrincePal** with the *--concurrent_jobs* attribute.  
    **NOTE:** The number of concurrent conversion, removal, and preview jobs defaults to 12. You can use this attribute with other attributes.