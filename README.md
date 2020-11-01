# Resume Parser named "PARSEIT" (<a href="https://drive.google.com/file/d/13AkZ3zfdjUtgDi20kPXIAmGAVGG3PB_Y/view?usp=sharing"><small>Demo Video</small></a>)
"PARSEIT" is a Resume Parsing webapp which can be used by firms to parse the applicant's resume (unstructured) in order to obtain a CSV file(structured) containing only the required information.
<pre>
Tech Used-
Django Framework, Python, Regex, File handling
</pre>

It takes resume in PDF document as an input and gives you the following results:
- Name
- Email address
- Phone number 
- LinkedIn profile url  
- Total No. of Text Lines + Total No. of Text characters present in the document.
After running the application, it gives you an option to download the .csv file
<pre>
Workflow -
pdf file --> text file --> details extracted using pattern matching --> write the obtain details in a CSV file
</pre>
<!-- Explanatory Document
https://drive.google.com/file/d/1hMLKw7NfM7dATq0oaVeQzCF1V4nwNO6c/view?usp=sharing
-->

<pre>
Resume_Parser (contains all project files)
|_   app (app name) - _pycache_ , migrations ,
|    static (contains all static files like .css and .js files) ,
|    templates (contains .html files) ,
|    url(contains all paths),
|    views.py (corresponding to each url a view is created),
|    convertor.py (contains logic for conversion of pdf to .txt),
|    extract.py (contains code to extract various fields),
|    createcsv (it is a .py file that contains logic for storing of extracted 
|
|_   media - After receiving the uploaded files from user the files are saved here, path
|    has been mendioned in views.py. It has two other folders -
|    1. txtfiles this folder stored files after they are converted to .txt form by convertor.py
|    2. csvfiles contains csv files that user can download which are sent to this path by createcsv.py
|
|_   Resume_Parser – contains other project files most imp one being settings.py
|
|_   manage.py
</pre>
 
