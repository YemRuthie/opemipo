# code to input name age and calculate year to be a 100
from datetime import date 

def calculateyear(birthyear,hundredin): 
    # take in name
    name = str(input("Enter name: "))

    #take in curent age
    age= int(input("Enter age: "))
 
    today = date.today()
    
    birthyear= today.year - age
    
    hundredin = birthyear + 100
    
    print ("your name is ",name,", you are ",age,", you were born in ",birthyear,", you will be 100 in ", hundredin)
    
    return ;

calculateyear (10,10)



