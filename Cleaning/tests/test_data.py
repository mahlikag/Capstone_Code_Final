#The following is the code that was used to clean the Stata data



#These are the codes from the codebook found in the zipfile from the nacjd database
#int variables (eg. 2014)
year = 2016

#str variables (eg. 'BH019')
#CITY NAME code
city = 'BH007'

#STATE ABBREVIATION code
state = 'BH008'

#CURRENT POPULATION 1 code
population = 'BH019'


#UCR OFFENSE CODE - 1
UCR1 = 'V20061'

#UCR OFFENSE CODE - 2
UCR2 = 'V20062'

#UCR OFFENSE CODE - 3
UCR3 = 'V20063'


#TYPE WEAPON/FORCE INVOLVED 1-1
weapon1_1 ='V20171'

#TYPE WEAPON/FORCE INVOLVED 1-2
weapon1_2 ='V20172'

#TYPE WEAPON/FORCE INVOLVED 1-3
weapon1_3 ='V20173'

#TYPE WEAPON/FORCE INVOLVED 2-1
weapon2_1 ='V20181'

#TYPE WEAPON/FORCE INVOLVED 2-2
weapon2_2 ='V20182'

#TYPE WEAPON/FORCE INVOLVED 2-3
weapon2_3 ='V20183'

#TYPE WEAPON/FORCE INVOLVED 3-1
weapon3_1 ='V20191'

#TYPE WEAPON/FORCE INVOLVED 3-2
weapon3_2 ='V20192'

#TYPE WEAPON/FORCE INVOLVED 3-3
weapon3_3 ='V20193'

#UCR ARREST OFFENSE CODE - 1
UCR_arrest1 = 'V60111'

#UCR ARREST OFFENSE CODE - 2
UCR_arrest2 = 'V60112'

#UCR ARREST OFFENSE CODE - 3
UCR_arrest3 = 'V60113'

number_of_cities = 100

#this is the list of weapons that are firearm or gun related
weapons_list = ['Handgun-automatic', 'Rifle', 'Other Firearm', 'Firearm (type not stated)', 'Handgun', 'Rifle-automatic', 'Firearm-automatic', 'Other Firearm-automatic', 'Shotgun', 'Shotgun-automatic']



#The following imports the data function from the Cleaning directory and saves the produced dataframe from the get_new_Data() function
from Cleaning.data import get_new_Data
new_Data = get_new_Data(year,city,state,population,weapons_list,UCR1,UCR2,UCR3,weapon1_1,weapon1_2,weapon1_3,weapon2_1,weapon2_2,weapon2_3,weapon3_1,weapon3_2,weapon3_3,UCR_arrest1,UCR_arrest2,UCR_arrest3,number_of_cities)

#The following imports the data function from the Cleaning directory and saves the produced dictionary from the calculate_rates

Data_Values = {}
from Cleaning.data import calculate_rates
Data_Values = calculate_rates(Data_Values,new_Data,city,UCR1,UCR2,UCR3,UCR_arrest1,UCR_arrest2,UCR_arrest3,number_of_cities)

#saving all of the new entries in the dictionary so they can be used for the storing_rates function
Counted = Data_Values['Counted']
aa = Data_Values['aa']
murder = Data_Values['murder']
robbery = Data_Values['rob']
aa_Clear = Data_Values['aa_Clear']
murder_Clear = Data_Values['murder_Clear']
robbery_Clear = Data_Values['robbery_Clear']


#The following imports the data function from the Cleaning directory and saves the produced dictionary from the recording_rates
from Cleaning.data import storing_rates
Data_Values = storing_rates(Data_Values,new_Data,city,state,population,Counted,aa,murder,robbery,aa_Clear,murder_Clear,robbery_Clear,number_of_cities)


#creating the tests for data

#testing if there are only 100 different cities in the dataframe
def test_get_new_Data():
    assert len(new_Data[city].unique()) == 100 

#testing if there are 100 different incident numbers in the AA list
def test_calculate_rates():
    assert len(Data_Values['aa']) == 100

#testing if there are 100 different clearance rates in the AA_Clear list
def test_storing_rates():
    assert len(Data_Values['aa_clearance_rate']) == 100
    
