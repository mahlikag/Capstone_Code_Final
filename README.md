# Capstone_Code

The following are some instructions on how to best execute the data cleaning, DBSCAN, and network files. You will need Python for these files, I recommend Anaconda but please choose what you're most comfortable with.
You will also need to download a couple of files from the internet as well in this repository.


DOWNLOADING THE FILES:


To download the data, please go to https://www.icpsr.umich.edu/web/NACJD/series/128

*You'll have to make an account for this website*

You can click on any year's file from 2007 to 2016 (but for an easier process I would suggest 2014, 2015, or 2016). Please download the "Extract Files" version. I.e National Incident-Based Reporting System, 2015: Extract Files. Once you click on the link, you will be taken to a page for download.
I recommend instead of hitting the first download tab, click on the "Data & Documentation tab". Then look for "DS1 Incident-Level File" and click the download arrow associated with that row. This just makes sure you download the bare minimum need since the file is already large. You want your download to be in Stata format. Once it's downloaded, unzip the folder. From here you only need two things from this extracted folder. 
The first is the Codebook (named “xxxxx-Codebook”) and the second is the actual .dta file (named “xxxxx-0001-Data.dta”) which is located in the “DS0001” folder. Take both of these files and put them in the Data folder from the repository you just downloaded. There should already be a file in there titled "2007-2016.xlsx" but after you moved those two files over, the folder should have one .dta file, one .pdf file, and one .xlsx file, a total of 3 files.

Make sure this Data folder is in no other folder but the Capstone_Code_Final folder. And change the name of the “xxxxx-0001-Data.dta” file in the Data folder to whatever year you downloaded (i.e from “37066-0001-Data.dta” to "2016.dta")

From there, the preliminary files have been set up!
 
RUNNING CleaningData.py:


This file was used to clean yearly data. One by one, I downloaded each year's data and copied the resulting excel file and pasted it into a larger excel file that separated each of the years in different tabs. For testing purposes, you can just download data from one year (seeing that the files are at least 4.5 GB) and downloading for all 100 might be tedious.
Before running this file, please make sure you have the packages panda and numpy downloaded for Python. These files will be imported in the programs so ensuring that you have it installed will prevent errors.


************ If you downloaded a file from any year between 2014 and 2016 ignore the next step and move on to the next (*) ************


Now that you have the files, you're going to need to edit the first part of the python file. In the folder that you created named Data, open the Codebook. You’ll use the codes on pages 12 - 25 to determine the codes that need to be changed in the first part of the python file. For example, for the year 2008, Current Population 1 is no longer BH019 but B2005. Change any of the codes that need to be changed. You can use the comment above the code variable to search for the desired variable in the codebook. (The codes needing changing should at least be city, state,  and current population).

* Now you can run the file! It should produce a new excel sheet title "year"+Data.xlsx. 
As previously stated, I used this to get the ‘2007-2016.xlsx’ file but for your convenience, I included that in the repository and that will be the file we’re going to extract information from moving forward. 
 
RUNNING DBSCAN: 

Before running the python file, make sure you have the '2007-2016.xlsx' file downloaded in your working directory. 
 
The DBSCAN file should print some information about each city as well as the DBSCAN graphs for each of the 10 years.


RUNNING NETWORKS:

Before running the python file, you while need to install the following programs if they are not already installed on your computer:
Read_excel (by using the command 'pip install xlrd')
NetworkX (by using the command 'pip install networkx')
Matplotlib (by using the command 'pip install matplotlib')
Pandas (by using the command 'pip install pandas')
You can then open the Networkx.py file and run the program!!
Python should produce a total of 10 graphs, one for each of the 10 years of study.


TESTING THE FUNCTIONS: 

To test the function easily, I created a directory titled tests with all of my tests. All you have to do is set your working directory in the shell or terminal to the directory you have the files downloaded from the repository in. Then type “python -m pytest Cleaning”. This may take anywhere from 5 - 10 minutes just because the reading of the file in the CleaningData file takes a minute but all 5 tests should result in a pass. 

And that’s it! Thanks for running my code!!

