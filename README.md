# Analyzing the Crime Profile of Clustering Cities

In the recent years, data science techniques have transcended beyond topics of software. One of these topics being that of criminal justice. These said techniques were used to delve into realm of criminal justice in an attempt to discover possible parallels between various attributes of cities within the US (population size, location, etc) and their ability to solve crimes(clearance rates). Using a python library called NetworkX, network connections were shown through graphs. Overall, the goal was to prove connections between clearance rates and certain individual attributes. This way, an idea of what makes a city naturally have a higher clearance rate would be uncovered and could potentially create guidelines that would better aid them in handling crime for a city like theirs.


The following are some instructions on how to best execute the files:
* data cleaning
* DBSCAN 
* NetworkX

# Requirements

You will need Python for these files, I recommend Anaconda but please choose what you're most comfortable with.

You will also need to download a couple of files from the internet as well in this repository.

## Package Requirements 
Before running the python files, you while need to install the following programs if they are not already installed on your computer:

* Read_excel (by using the command 'pip install xlrd')
* NetworkX (by using the command 'pip install networkx')
* Matplotlib (by using the command 'pip install matplotlib')
* Pandas (by using the command 'pip install pandas')

# File Setup

## Downloading the Files

To download the data, please go to https://www.icpsr.umich.edu/web/NACJD/series/128

*You'll have to make an account for this website*

You can click on any year's file from 2007 to 2016 (but for an easier process I would suggest 2014, 2015, or 2016). 

1) Please download the "Extract Files" version. I.e National Incident-Based Reporting System, 2015: Extract Files. 

*Once you click on the link, you will be taken to a page for download.* 

2) I recommend instead of hitting the first download tab, click on the "Data & Documentation tab". 

3) Then look for "DS1 Incident-Level File" and click the download arrow associated with that row. This just makes sure you download the bare minimum needed since the file is already large. 

4) You want your download to be in Stata format. Once it's downloaded, unzip the folder. 


## Setting up your folders

From here you only need two things from this extracted folder. 

* The first is the Codebook (named “xxxxx-Codebook”)
* The second is the actual .dta file (named “xxxxx-0001-Data.dta”) which is located in the “DS0001” folder

1) Take both of these files and put them in the Data folder from the repository you just downloaded. 

### Note: There should already be a file in there titled "2007-2016.xlsx", but, after you moved those two files over, the folder should have one .dta file, one .pdf file, and one .xlsx file, a total of 3 files.

2) Double check that the Data folder is in no other folder but the Capstone_Code_Final folder.

3) Change the name of the “xxxxx-0001-Data.dta” file in the Data folder to whatever year you downloaded (i.e from “37066-0001-Data.dta” to "2016.dta")

From there, the preliminary files have been set up!

# .PY File Instructions
 

## CleaningData.py:


* This file was used to clean yearly data. One by one, I downloaded each year's data and copied the resulting excel file and pasted it into a larger excel file that separated each of the years in different tabs. 

* For testing purposes, you can just download data from one year (seeing that the files are at least 4.5 GB) and downloading for all 100 might be tedious.

* Before running this file, please make sure you have the packages panda and numpy downloaded for Python. These files will be imported in the programs so ensuring that you have it installed will prevent errors.


### Note: If you downloaded a file from any year between 2014 and 2016 ignore the next bullet points and move to the first step


* Now that you have the files, you're going to need to edit the first part of the python file. 
* In the folder that you created named Data, open the Codebook. 
* You’ll use the codes on pages 12 - 25 to determine the codes that need to be changed in the first part of the python file. For example, for the year 2008, Current Population 1 is no longer BH019 but B2005. 
* Change any of the codes that need to be changed. You can use the comment above the code variable to search for the desired variable in the codebook. (The codes needing changing should at least be city, state,  and current population).

1) Now you can run the file in Anaconda! It should produce a new excel sheet title "year"+Data.xlsx in your working directory.


*As previously stated, I repeated this 10 times to get the values for all 10 years. But for your convenience, I included the finished ‘2007-2016.xlsx’ file in the repository's Data folder and that will be the file we’re going to extract information from moving forward. 

 
## DBSCAN 

**Friendly Reminder:** Before running the python file, make sure you have the '2007-2016.xlsx' file downloaded in the Data folder. 

Once you run the DBSCAN file in anaconda, you should see:

* the printed cluster groups of the cities for each year
* DBSCAN graphs for each of the 10 years


## Networks

**Friendly Reminder:** Before running the python file, make sure you have the '2007-2016.xlsx' file downloaded in the Data folder.


Once you run the Netowrks file in anaconda, you should see:

* a total of 10 graphs, one for each of the 10 years of study of the clusters


# Tests 

To test the function easily, I created a directory titled tests with all of my tests. 

All you have to do is set your working directory in the shell or terminal to the directory you have the files downloaded from the repository in

By using pytests, you wont have to run each test individually. All of the tests in the test folder will run consecutively. 

Type:

```
python -m pytest Cleaning

```
This may take anywhere from 5 - 10 minutes just because the reading of the file in the CleaningData file takes a minute but all 5 tests should result in a pass. 

And that’s it! Thanks for running my code!!

