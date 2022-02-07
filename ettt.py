import os
from pickletools import string1
import platform
from re import I, M
from runpy import run_path
from tkinter import N, Y
from pylab import *
import sys
import re
import math
import argparse
 
  
from functools import reduce

def manage(): #Function For The Student Management System

	x = "#" * 30
	y = "=" * 28
	global bye #Making Bye As Super Global Variable
	bye = "\n {}\n# {} #\n# ===> Brought To You By <===  #\n# ===> code-projects.org <===  #\n# {} #\n {}".format(x, y, y, x) # Will Print GoodBye Message


print (""" ----------------------------------------------------------------------
 |=====================================================================| 
 |=========== Wellcome all in public science museum  ==================|
 |=====================================================================|
  ----------------------------------------------------------------------
  
  
  Patron Type
Enter 1 :  Science Rookie
Enter 2 :  Science Enthusiast""")

try: #Using Exceptions For Validation
		userInput = int(input("Please Select An Above Option: ")) #Will Take Input From User
except ValueError:
		exit("\nHy! That's Not A Number") #Error Message
else:
		print("\n") #Print New Line

	#Checking Using Option	
if(userInput == 1): #This Option Will Print List Of Students
		print("""The vast plains of the Serengeti comprise 1.5 million ha of savannah. The annual migration to permanent water holes of vast herds of herbivores (wildebeest, gazelles and zebras),
followed by their predators, is one of the most impressive natural events in the world.\n
 """)  
	#Checking Using Option	
elif(userInput == 2): #This Option Will Print List Of Students
		print("""The vast plains of the Serengeti comprise 1.5 million ha of savannah. The annual migration to permanent water holes of vast herds of herbivores (wildebeest, gazelles and zebras),
followed by their predators, is one of the most impressive natural events in the world.\n """)  

m = print (input("animal mass:"))
t = print (input("Top speed:"))
sec_to_hr = 1/3600 # 3600 seconds in 1 hour
min_to_hr = 1/60 # 60 minutes in 1 hour
km_to_miles = 1/1000 #   in 1 kilometer

t_hrs = 1 + (5*min_to_hr) + (42*sec_to_hr)  # Total time in hours
dist_miles = 10 * km_to_miles # Total time in miles

m_speed = dist_miles/t_hrs #  Speed in miles/hour

answer1 = "motion = {} meter per hour".format(round(m_speed,2))

print(answer1)

def ms():
    	print("As predator populations increase, they put greater strain on the prey populations and act as a top-down control, pushing them toward a state of decline. Thus both availability of resources and predation pressure affect the size of prey populations. ")
ms()

def run (): #Making Runable Problem1353
	run = input("\n Enthusiast? Y/n: ")
	if(run.lower() == 'y'):
		if(platform.system() == "Windows"): #Checking User OS For Clearing The Screen
			print("the dynamics of a modified predator-prey BB model with Allee effects and seasonal perturbation are studied in depth. New bifurcation sites, such as limit point cycle and period-doubling bifurcations, as well as those identified by modelling the prey's growth rate and predator efficiency using modified algebraic structures, are discovered in addition to the Hopf bifurcation.") 
		else:
			print(os.system('clear'))
		manage()
run ()

def doc():
    	doc = input("an initial separation between predator and prey: ")
m = print (input("animal mass:"))
t = print (input("Top speed:"))
print(answer1)
doc()

def rerun (): #Making Runable Problem1353
	rerun = input("\n Enthusiast? Y/n: ")
	if(rerun.lower() == 'y'):
		if(platform.system() == "Windows"): #Checking User OS For Clearing The Screen
				print("the dynamics of a modified predator-prey BB model with Allee effects and seasonal perturbation are studied in depth. New bifurcation sites, such as limit point cycle and period-doubling bifurcations, as well as those identified by modelling the prey's growth rate and predator efficiency using modified algebraic structures, are discovered in addition to the Hopf bifurcation.") 
		else:
			print(os.system('clear'))
         
rerun()		 


def runAgain(): #Making Runable Problem1353
	runAgn = input("\n Enthusiast? Y/n: ")
	if(runAgn.lower() == 'y'):
		if(platform.system() == "Windows"): #Checking User OS For Clearing The Screen
			print("Animal models are actually a critical part of biological research, because if you imagine, experimentation on humans is at least frowned upon and actually really more likely prohibited in most of the kinds of things that we want to do. We need a stand-in of some sort, so scientists rely on the conservation of processes, biological processes, that occur across all species, or some species, and we use a variety of them.") 
		else:
			print(os.system('clear'))
		manage()
		runAgain()
	else:
		print("Thank you visit again") #Print GoodBye Message And Exit The Program

runAgain()	

 

 
	   

			


    
        

    		

     
    