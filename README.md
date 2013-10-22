Stide-ADS
=========

System Call based Anomaly Detection System
Python - STIDE technique (sequence time-delay embedding)


This was a project for my data mining class.

If you're doing Anomaly Detection System based on Linux System Call level sequence analysis or anything related to system call sequences this may come in handy.



DESCRIPTION OF FILES
====================


-+ Presentation and Paper
------ Presentation.pdf
------ FInal Report.pdf

--> Problem description and details regarding the dataset and methods.


-+ Sample Data
-----+ Anubis-good
-----+ Malware

-->Sample files from the dataset used in this project.
	for further information you can check these links:
		http://anubis.iseclab.org/
		http://anubis.iseclab.org/?action=publications
	
	
-+ Sample outputs

--> Sample output files from the python folder.


-+ Python files

------ compare_STIDE.py
->STIDE technique implementation with Python

------ SysCallExtract.py
-> Extract system call number sequences from the Anubis Dataset
you can change the window size and the shift size by changing the W and K values



LICENSE
========
The MIT License (MIT)

Copyright (c) 2013 Shayan Eskandari

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
