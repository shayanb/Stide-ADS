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


