# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 17:46:35 2020

@author: Matthew Merritt

Description:
    Virus S.I.R. modeling. The program through user input of an infection and
    recovery rate are capable of seeing the impact that these factors play in 
    the populations of the number of suspectptibles, Infectives, and Removed
    in a day (These terms are defined below).
    
    Terms:
        S(t) : number of susceptible on day t
        I(t) : the number of infectives on day t
        R(t) : the number of removed on day t
        
        a = recovery rate
        b = Infection Rate
        
        #Formulas:
            b*S(t)*I(s) : number of susceptibles that get infected
            a*I(t) : nuber infecteds that get removed
        
        
        Next Generation Formulas:
            S(t+1) - S(t) = -b*S(t)*I(t) : change in the number susceptibles
            I(t+1) - I(t) = b*S(t)*I(t) - a*I(t): change in the number of infected
            R(t+1) - R(t) = a*I(t): change in the number removed
        
    Definitions:
        -Susceptible(S): A person who is what would be called healthy and is not
        infected.
        -Infectives(I): A person who is what would be called infected and is 
        capable of spreading the virus.
        -Removed(R): A person who would be called dead or immune to the disease, 
        who no longer has the virus and are "immune" to the virus.
    
"""


import numpy as np
import matplotlib.pyplot as plt



class SIR_Model(object):
    '''
    This is a class for using SIR modeling with the capbilities 
    
    '''
    
    def __init__(self, susceptibles=20000, infectives=100, removed=0, infectionRate=0.00005, recoveryRate=0.1, daysLoaded=20):
        '''
        
        Description:
            This class is of a S.I.R. model, with capabilities to graph calculated
            data over a selected amount of days.
        Input:
            susceptibles : int
            infectives : int
            removed : int
            infectionRate : float
            recoveryRate : float
            daysLoaded : int
        Output:
            None : none
                Instance of SIR_Model class

        '''
        #populations
        self.susceptibles = susceptibles
        self.infectives = infectives
        self.removed = removed
        
        #rates
        self.infectionRate = infectionRate
        self.recoveryRate = recoveryRate
        
        #other
        self.logDictionary = {'day_0':[susceptibles, infectives, removed]}#format [susceptibles, infected, removed]
        self.daysLoaded = daysLoaded
        
        #loads first 20 days of predicted simulation
        self.update(daysLoaded)
        
        
    def __str__(self):
        '''
        
        Description:
            This funciton returns a string contatining susceptibles, infected, removed 
            amounts for each day along with the infection and recovery rates.
        Input:
            
        Output:
            This funciton returns a string contatining susceptibles, infected, removed 
            amounts for each day.

        '''
        outputString = '-'*60 + '\n'
        outputString += '{:^30}{:^30}\n'.format('infection Rate' + str(self.infectionRate), ('Recovery Rate' + str(self.recoveryRate)))
        
        
        outputString += '-'*60 + '\n'
        outputString += ' '*10   + '{:^15}{:^15}{:^15} \n'.format('susceptibles', 'infected', 'removed' )
        for day in range(len(self.logDictionary)):
            outputString += '-'*60 +'\n'
            outputString += 'day {:^4} : {:^15}{:^15}{:^15}\n'.format(day, 
                            self.logDictionary['day_'+str(day)][0], self.logDictionary['day_'+str(day)][1], self.logDictionary['day_'+str(day)][2])
            outputString += '-'*60 + '\n'
            
        outputString +='{} have been loaded\n'.format(len(self.logDictionary))
        return outputString
    
    
    def update(self, days=20):#load x amount of days #returns a dict of each dat
        #the amount of days that should pass
        '''
        Description:
            This function calculates the model up to the day argument
        Input:
            days : int
                The amount of days that have passesed since the instantiation of the simulated virus.
        Output:
            None : none
        '''
        Sus = self.susceptibles
        Inf = self.infectives
        Rem = self.removed

        nextSus = 0
        nextInf = 0
        nextRem = 0
    
        #create logs for days
        for day in range(1,days+1):
            
            #get next generation
            nextSus = int(Sus - self.infectionRate*Sus*Inf)
            nextInf = int(Inf + ( self.infectionRate*Sus*Inf - self.recoveryRate*Inf ))
            nextRem = int(Rem + self.recoveryRate*Inf)
            
            #log data
            self.logDictionary['day_'+str(day)] = [nextSus, nextInf, nextRem]
            
            #update variables
            Sus = nextSus
            Inf = nextInf
            Rem = nextRem
    
    
    def get_susceptibles(self, day=0):#set so if no day an average?
        '''
        Description:
            This function returns the amount of the population which is becomes susceptibles.
            If no day is specified then it returns the first day.
        Input:
            day : int
                The amount of days since the start of the outbreak.
        Output:
            susceptibles : int
                 the amount of the population which is susceptible on the day choosen.
        '''
        return self.logDictionary['day_'+str(day)][0]
    
    
    def plot(self):
        '''
        Description:
            Using the matplot and numpy libraries, the population data for 
            infected, suspectable, and removed are graphed. 
        Inputs:
            none : none
        Output:
            graph : img
                A graph of population data over the loaded days
        '''
        
        #format data for graph
        time_map = list(range(len(self.logDictionary)))
        susLogs = list()
        infLogs = list()
        remLogs = list()
        for day in range(len(self.logDictionary)):
            susLogs.append(self.logDictionary['day_'+str(day)][0])
            infLogs.append(self.logDictionary['day_'+str(day)][1])
            remLogs.append(self.logDictionary['day_'+str(day)][2])
            
        susLogs = np.array(susLogs)
        infLogs = np.array(infLogs)
        remLogs = np.array(remLogs)
            
        #plot infection rate, recovery rate
        fig = plt.figure()
        ax = fig.add_subplot(111)
        fig.subplots_adjust(top=0.85)
        
        #add titles
        fig.suptitle('SIR Simulation')
        ax.set_title('Recovery Rate: {}, Infection Rate: {}'\
                .format(self.recoveryRate, self.infectionRate))
        
        #plot data
        plt.plot(time_map, susLogs, 'b-', label='Susceptible population')
        plt.plot(time_map, infLogs, 'g-', label='Infection population')
        plt.plot(time_map, remLogs, 'r-', label='Removed population')
        
        #create legend   
        plt.plot(loc='upper left')
        plt.xlabel('Time (In Days)')
        plt.ylabel('People')
        plt.legend()
    
    
if __name__ == "__main__":
    model = SIR_Model()
    print(model)
    
    