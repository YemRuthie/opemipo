import random

comp_choice = random.randint(1,9)

guess = int(input("type your guess: ")) 

if comp_choice == guess: 
		print ('you are right')
elif comp_choice > guess:
		print ('its lower than i picked')
else: 
		print ('itsn higher than i picked')		

print (comp_choice)
