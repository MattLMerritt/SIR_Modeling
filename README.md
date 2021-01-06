# SIR_Modeling
This project is for modeling a virus using the SIR modeling system based on a fixed population with sub populations of susceptible, infected, removed peoples. 

This is a program for a SIR model class in python that can be used to simulate a virus given parameters of:

    *susceptibles 
    *infectives 
    *removed 
    *infectionRate 
    *recoveryRate 
    *daysLoaded 

The class also has a graphing feature using the Matplot and Numpy libraries.

*Description:*

   *Virus S.I.R. modeling. The program through user input of an infection and recovery rate are capable of seeing the impact that these factors play in the populations of the number of suspectptibles, Infectives, and Removed in a day (These terms are defined below).
   	
1.Terms:
    
    *S(t) : number of susceptible on day t
    *I(t) : the number of infectives on day t
    *R(t) : the number of removed on day t
    *a = recovery rate
    *b = Infection Rate
       
2.Formulas:
    
    *b\*S(t)\*I(s) : number of susceptibles that get infected
    *a\*I(t) : nuber infecteds that get removed
        
3.Formulas for Next Generation:
    
    *S(t+1) - S(t) = -b\*S(t)\*I(t) : change in the number susceptibles
    *I(t+1) - I(t) = b\*S(t)\*I(t) - a\*I(t): change in the number of infected
    *R(t+1) - R(t) = a\*I(t): change in the number removed
        
##Definitions:
    
    *Susceptible(S): A person who is what would be called healthy and is not infected.
    *Infectives(I): A person who is what would be called infected and is 
    capable of spreading the virus.
    *Removed(R): A person who would be called dead or immune to the disease, 
    who no longer has the virus and are "immune" to the virus.

