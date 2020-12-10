"""importing the required packages"""
import pandas as p
import numpy as np



def get_new_Data(yr,city,state,pop,w_lst,UCR1,UCR2,UCR3,w1_1,w1_2,w1_3,w2_1,w2_2,w2_3,w3_1,w3_2,w3_3,UCR_arrest1,UCR_arrest2,UCR_arrest3,num):
    """reading the specified year's file and ordering it by population"""
    my_Data = p.read_stata('Data/'+str(yr)+'.dta')
    my_Data = my_Data.sort_values(by=[pop],ascending=False,na_position='last')

    """
    this command creates a new variable, Data, that only includes the incidents that involved one of the weapons in our weapons list
    this is because we are only focusing on incidents involving firearms in this study
    """
    
    Data = my_Data[(my_Data[w1_1].isin(w_lst)) | (my_Data[w1_2].isin(w_lst)) | (my_Data[w1_3].isin(w_lst)) 
                 | (my_Data[w2_1].isin(w_lst)) | (my_Data[w2_2].isin(w_lst)) | (my_Data[w2_3].isin(w_lst))
                 | (my_Data[w3_1].isin(w_lst)) | (my_Data[w3_2].isin(w_lst)) | (my_Data[w3_3].isin(w_lst))]
    """
    initializing the variables
    City is the column in the dataframe Data that matches the provided code
    """
    City = eval('Data.'+city)

    """State is the column in the dataframe Data that matches the provided code"""
    State = eval('Data.'+state)

    """Population is the column in the dataframe Data that matches the provided code"""
    Population = eval('Data.'+pop)

    cities = []
    key = []
    
    """
    creating a list of the first 100 unnique city occurences
    also using the population as the key
    if two different cities have the same name (i.e Lowell, MA and Lowell, AR) the population will help to differentiate
    thus having the identity key be a list of the populations
    """
    
    i = 0
    while len(cities)<num:
        if City.iloc[i] not in cities:
            cities.append(City.iloc[i])
            key.append(Population.iloc[i])
        i = i + 1

    """creating a new column entitled row_num that assigns a number to each row"""
    Data['row_num'] = np.arange(len(Data))

    iny = Data.loc[max(Data[Population == key[num-1]].index.values)].row_num
    return Data[:iny]

"""creating a function that will check if any of the crime columns match the specified crime"""
def crime_checker(crime,code1,code2,code3,new_Data,i):
    return (new_Data[code1].iloc[i]==crime or new_Data[code2].iloc[i]==crime or new_Data[code3].iloc[i] == crime)

            
     
    
"""this function calculates the number of incidents of each crime and returns them"""
def calculate_rates(Values,new_Data,city,UCR1,UCR2,UCR3,UCR_arrest1,UCR_arrest2,UCR_arrest3,num):
    """initilizaing variables as None for all 100 cities"""
    Counted = [None] * num
    sums = [None] * num
    aa = [None] * num
    aa_Clear = [None] * num
    murder = [None] * num
    murder_Clear = [None] * num
    rob = [None] * num
    robbery_Clear = [None] * num
    ind = 0
    
    while ind < 99:
        for i in range(len(new_Data)): 
            if new_Data[city].iloc[i] not in Counted:
                Counted[ind] = new_Data[city].iloc[i]
                sums[ind] = 1

                """if the offense code is 91, it is a murder. We initialize the murder count to 1 and stop checking. """
                if (crime_checker('Murder/Nonnegligent Manslaughter',UCR1,UCR2,UCR3,new_Data,i)):
                    murder[ind] = 1
                    
                """if there is an arrest, set the amount of cleared incidents to 1, and 0 otherwise"""
                    if(crime_checker('Murder/Nonnegligent Manslaughter',UCR_arrest1,UCR_arrest2,UCR_arrest3,new_Data,i)):
                        murder_Clear[ind] = 1
                    else:
                        murder_Clear[ind] = 0    

                """if the offense code is 131, it is an aggravated assault. We initialize aa to 1 and stop checking"""
                elif (crime_checker('Aggravated Assault',UCR1,UCR2,UCR3,new_Data,i)):
                    aa[ind] = 1
                    
                    """if there is an arrest, set the amount of cleared incidents to 1, and 0 otherwise"""
                    if(crime_checker('Aggravated Assault',UCR_arrest1,UCR_arrest2,UCR_arrest3,new_Data,i)):
                        aa_Clear[ind] = 1
                    else:
                        aa_Clear[ind] = 0 

                """if the offense code is 120, it is a robbery. We initialize robbery to 1 and stop checking"""
                elif (crime_checker('Robbery',UCR1,UCR2,UCR3,new_Data,i)):
                    rob[ind] = 1
                    
                    """if there is an arrest, set the amount of cleared incidents to 1, and 0 otherwise"""
                    if(crime_checker('Robbery',UCR_arrest1,UCR_arrest2,UCR_arrest3,new_Data,i)):
                        robbery_Clear[ind] = 1
                    else:
                        robbery_Clear[ind] = 0 

                """move to the next index"""       
                ind = ind + 1


        """if that city has already been added to the list... """
            else:
                """add one to the current incident count"""
                sums[Counted.index(new_Data[city].iloc[i])] = 1 + int(sums[Counted.index(new_Data[city].iloc[i])])

                """if its a murder, add one to the current murder count """
                if (crime_checker('Murder/Nonnegligent Manslaughter',UCR1,UCR2,UCR3,new_Data,i)):  
                    if (murder[Counted.index(new_Data[city].iloc[i])] == None):
                        murder[Counted.index(new_Data[city].iloc[i])] = 1
                    else:
                        murder[Counted.index(new_Data[city].iloc[i])] = 1 + int(murder[Counted.index(new_Data[city].iloc[i])])

                    """if there is an arrest, add 1 to cleared incident"""
                    if(crime_checker('Murder/Nonnegligent Manslaughter',UCR_arrest1,UCR_arrest2,UCR_arrest3,new_Data,i)):       
                        if (murder_Clear[Counted.index(new_Data[city].iloc[i])] == None):
                            murder_Clear[Counted.index(new_Data[city].iloc[i])] = 1
                        else:
                            murder_Clear[Counted.index(new_Data[city].iloc[i])] = 1 + int(murder_Clear[Counted.index(new_Data[city].iloc[i])])

                """if its an aggravated assault, add one to the current count """
                elif (crime_checker('Aggravated Assault',UCR1,UCR2,UCR3,new_Data,i)):    
                    if (aa[Counted.index(new_Data[city].iloc[i])] == None):
                        aa[Counted.index(new_Data[city].iloc[i])] = 1
                    else:
                        aa[Counted.index(new_Data[city].iloc[i])] = 1 + int(aa[Counted.index(new_Data[city].iloc[i])])                                                                                                                                

                    """if there is an arrest, add 1 to cleared incident"""
                    if(crime_checker('Aggravated Assault',UCR_arrest1,UCR_arrest2,UCR_arrest3,new_Data,i)):
                        if (aa_Clear[Counted.index(new_Data[city].iloc[i])] == None):
                            aa_Clear[Counted.index(new_Data[city].iloc[i])] = 1
                        else:
                            aa_Clear[Counted.index(new_Data[city].iloc[i])] = 1 + int(aa_Clear[Counted.index(new_Data[city].iloc[i])])                                                             

                """if its a robbery, add one to the current robbery count """
                elif (crime_checker('Robbery',UCR1,UCR2,UCR3,new_Data,i)):
                    if (rob[Counted.index(new_Data[city].iloc[i])] == None):
                        rob[Counted.index(new_Data[city].iloc[i])] = 1
                    else:
                        rob[Counted.index(new_Data[city].iloc[i])] = 1 + int(rob[Counted.index(new_Data[city].iloc[i])])                                                                 
                    """if there is an arrest, add 1 to cleared incident"""
                    if(crime_checker('Robbery',UCR_arrest1,UCR_arrest2,UCR_arrest3,new_Data,i)):
                        if (robbery_Clear[Counted.index(new_Data[city].iloc[i])] == None):
                            robbery_Clear[Counted.index(new_Data[city].iloc[i])] = 1
                        else:
                            robbery_Clear[Counted.index(new_Data[city].iloc[i])] = 1 + int(robbery_Clear[Counted.index(new_Data[city].iloc[i])])                                                             
                        
                        
    Values['Counted'] = Counted
    Values['sums'] = sums
    Values['aa'] = aa
    Values['aa_Clear'] = aa_Clear
    Values['murder'] = murder
    Values['murder_Clear'] = murder_Clear
    Values['rob'] = rob
    Values['robbery_Clear'] = robbery_Clear
    
    return Values  

"""this function calculates the clearance rates of each crime and returns them"""
def storing_rates(Values,new_Data,city,state,population,Counted,aa,murder,robbery,aa_Clear,murder_Clear,robbery_Clear,num):
    
    """Store the final city list as the Counted list"""
    final_city = Counted
    final_state = [0] * num
    final_population = [0] * num
    type_incidents = [None] * num
    crime_rate = [None] * num
    murder_perct = [None] * num
    murder_clearance_rate = [None] * num
    aa_perct = [None] * num
    aa_clearance_rate = [None] * num
    robbery_perct = [None] * num
    robbery_clearance_rate = [None] * num
    
    for i in range(len(final_city)):

        """For every city in the Counted list, add there corresponding State from the data frame, in the same matching index but within a new list "final_state"""
        final_state[i] = new_Data.loc[max(new_Data[new_Data[city] == final_city[i]].index.values)][state]

        """adding the populations to a list based on the cities"""
        final_population[i] = new_Data.loc[max(new_Data[new_Data[city] == final_city[i]].index.values)][population]

        """
        the specific type of incidents is the sum of the 3 interested crimes if none of them are None
        However, seeing that any one of them could be None, all combinations are ran to account for the different scenarios
        """
        
        if (aa[i]!=None and murder[i]!=None and robbery[i]!=None):
            type_incidents[i] = (aa[i]) + (robbery[i]) + (murder[i])

        elif (aa[i]==None and murder[i]==None):
            if(robbery[i]!=None):
                type_incidents[i] = robbery[i]

        elif (aa[i]==None and robbery[i]==None):
            if(murder[i]!=None):
                type_incidents[i] = murder[i]        

        elif (murder[i]==None and robbery[i]==None):
            if(aa[i]!=None):
                type_incidents[i] = aa[i]

        elif(aa[i]==None):
            type_incidents[i] = robbery[i] + murder[i]

        elif(murder[i]==None):
            type_incidents[i] = robbery[i] + aa[i]

        elif(robbery[i]==None):
            type_incidents[i] = aa[i] + murder[i]

        """crime rate is type incidents divided by population times 100000"""
        if type_incidents[i] !=None:
            crime_rate[i] = (int(type_incidents[i])/int(final_population[i])) * 100000

            """percentage of murders"""
            if(murder[i]!=None):
                murder_perct[i] = (int(murder[i])/int(type_incidents[i])) * 100
                if (murder[i]!=0 and murder_Clear[i]!=None):
                    murder_clearance_rate[i] = (int(murder_Clear[i])/int(murder[i]))*100

            """percentage of aggravated assaults"""
            if(aa[i]!=None):
                aa_perct[i] = (int(aa[i])/int(type_incidents[i])) * 100
                if (aa[i]!=0 and aa_Clear[i]!=None):
                    aa_clearance_rate[i] = (int(aa_Clear[i])/int(aa[i]))*100

            """percentage of robbery"""
            if(robbery[i]!=None):
                robbery_perct[i] = (int(robbery[i])/int(type_incidents[i])) * 100
                if (robbery[i]!=0 and robbery_Clear[i]!=None):
                    robbery_clearance_rate[i] = (int(robbery_Clear[i])/int(robbery[i]))*100


    Values['final_city'] = final_city
    Values['final_state'] = final_state
    Values['final_population'] = final_population
    Values['type_incidents'] = type_incidents
    Values['crime_rate'] = crime_rate
    Values['murder_perct'] = murder_perct
    Values['murder_clearance_rate'] = murder_clearance_rate
    Values['aa_perct'] = aa_perct
    Values['aa_clearance_rate'] = aa_clearance_rate
    Values['robbery_perct'] = robbery_perct
    Values['robbery_clearance_rate'] = robbery_clearance_rate
    
    return Values

