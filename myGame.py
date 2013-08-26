 #!/usr/bin/env python
import time
import sys
import random
import decimal

#Editing to try out github and ungit


#variable later used for printing strings in the compare functions.
actionprint = 0

#variable later used after obtaining the key from the drawer
haveKey1 = 0

#available after solving the lock
lock1_solved = 0

#available after beein to corridor
been_to_corrdior = 0

#These are variable for a possible fight module later down the road.
#HPmax = 50
player_HP = 50
#MPmax = 100
#MP = 100
#STmax = 25
#ST = 25
player_AD = 5

#function to print text out like a typewriter.
def typewrite(text) :
	#for each letter in text
	for a in text :
		#print out said letter
		sys.stdout.write(a)
		#then sleep
		time.sleep(0.06)
	#after printing letters, sleep
	time.sleep(0.3)

#slower version of typewrite
def typewriteslow(text) :
	for a in text :
		sys.stdout.write(a)
		time.sleep(0.15)
	time.sleep(0.3)

#faster version....
def typewritefast(text) :
	for a in text :
		sys.stdout.write(a)
		time.sleep(0.03)
	time.sleep(0.3)


#funciton for easy prompting throug out the whole game.
def promptme() :
	global next_command
	next_command = raw_input("> ")
	return next_command

#a funciton used to compare strings and if the strings are correct then print out action. If killswitch is on (1) then the person dies with the action message.
def compare (word1, word2, action, killswitch) :
	global actionprint
	if word1 in next_command.lower() and word2 in next_command.lower() and killswitch == 0 :
		actionprint = action + "\n"
		return word1 in next_command.lower() and word2 in next_command.lower()
	elif word1 in next_command.lower() and word2 in next_command.lower() and killswitch == 1 : 
		return dead(action)

#same function as above, but with the or logic
def compareor (word1, word2, action, killswitch) :
	global actionprint
	if (word1 in next_command.lower() or word2 in next_command.lower()) and killswitch == 0 :
		actionprint = action + "\n"
		return word1 in next_command.lower() or word2 in next_command.lower()
	elif (word1 in next_command.lower() or word2 in next_command.lower()) and killswitch == 1 : 
		return dead(action)

#functoin to exit the game, with a reason printed out
def exit(reason):
	typewrite(reason)
	sys.exit(0)

def bookshelfq():
	typewrite("Would you like to look open an other book?" + "\n")

	while True:
		promptme()
		if "yes" in next_command.lower() :
			typewrite("Which one?" + "\n")
			bookshelf1()
		if "no" in next_command.lower() :
			room1()
		else:
			typewritefast("Please answer with yes or no!" + "\n")

def bookshelf1():
	typewritefast("1, Book of black magic." + "\n")
	typewritefast("2, Book of potions." + "\n")
	typewritefast("3, Book of numbers." + "\n")

	while True:
		promptme()
		if compareor("1", "magic", "You open the book, but it is all written in a language that looks like latin. You don't understand anything.", 0):
			typewrite(actionprint)
			bookshelfq()
		elif compareor("2", "potions",'"Take one frogleg and an eye of a crow, some snail slime and mixe them together...', 0):
			typewrite(actionprint)
			typewrite("Ugh, you just put it back quick..."),time.sleep(0.2),typewrite("It sounds disgusting.")
			bookshelfq()
		elif compareor("3", "numbers", "You open the book and a paper falls out of it with the numbers on it:",0):
			typewrite(actionprint)
			typewriteslow("6 3 7" + "\n")
			bookshelfq()
		elif "back" in next_command.lower():
			room1()
		else :
			typewritefast("Please pick one of the books by choosing it's number, or go back!" + "\n")


def start():
	print "\n"
	""""typewriteslow("You feel cold." + "\n")
	time.sleep(0.4)
	typewrite("You open your eyes." + "\n")
	time.sleep(0.4)
	typewrite("You don't know where you are,"), typewrite(" or how you got here.")
	time.sleep(0.6)
	typewrite(" You stand up." + "\n")
	time.sleep(0.4)
	typewrite("By the looks of it, you found yourself in a room, in a castle." + "\n")
	time.sleep(0.5) """
	typewrite("What do you do?" + "\n")
	time.sleep(1)
	print "1, Look around in the room."
	time.sleep(0.9)
	print "2, Exit game."
	
	
	while True:
		promptme()
		if "1" in next_command.lower() :
			"""typewrite("You look around in the room."+"\n")
			time.sleep(0.5)
			typewrite("The room is only lit by a candle."+"\n")
			typewrite("The air is cold,"),typewrite(" you can hear the wind blowing and whistling outside. "+"\n")
			time.sleep(0.4)
			typewrite("The candle casts dancing shadows on the walls."),time.sleep(0.3),typewrite(" At least some source of warmth."+"\n")
			typewrite("You can see an old wooden door in front of you, with black iron fittngs that started to rust a little."+"\n")
			typewrite("To your right,"),time.sleep(0.5),typewrite(" there is a window with a curtain, some painting on the wall of a lake in a forest."+"\n")
			typewrite("To your left,"),time.sleep(0.5),typewrite(" there is a wall with a big bookshelf with many dusty books,"),typewrite("  some even covered with spider webs."+"\n")
			typewrite("Behind you,"),time.sleep(0.5),typewrite(" there is a big old wooden desk. Some papers are on it, and a pen."+"\n")"""
			typewrite('*Now you can use other commands. For a list of commands, type: "help"* any time during the game.' + "\n")
			room1()
		elif "2" in next_command.lower():
			exit("You decided to give up!" + "\n")
		else:
			typewrite("Please chose option: 1 or 2." + "\n")
			
	

def room1():
	typewrite("What would you like to do?" + "\n")
		

	global haveKey1
	
	
	while True :
		promptme()
		if "help" in next_command.lower():
			typewrite("The availble commands are:" + "\n")
			typewrite("Go" + "\n")
			#typewrite("Take" + "\n")
			typewrite("Open" + "\n")
			typewrite("Look" + "\n")
			typewrite("Scream" + "\n")
		
		elif compare("kick", "door", "The door opened!",0):
			typewrite("You step through the open door."+"\n")
			corridor1()

		elif "skipdoor" in next_command.lower():
			room2()

		elif (compare("go", "bookshelf", "You look at the bookshelf, there are several books on it.", 0) or compare("look", "bookshelf", "You look at the bookshelf, there are several books on it.", 0) or compare("look", "book","You look at the bookshelf, there are several books on it.", 0) or compare("open", "book", "You look at the bookshelf, there are several books on it." ,0)):
			typewrite(actionprint)
			typewrite("Three books catch your eyes. \nWhich one do you want to open?" + "\n")
			bookshelf1()

		elif (compare("look", "desk", "You look at the desk.\n It is an old desk, with some empty sheets on it, and a pen.\n You can also see a drawer on the desk, probably unlocked.", 0) or compare("go", "desk", "You look at the desk.\n It is an old desk, with some empty sheets on it, with a pen.\n You can also see a drawer of the desk, probably unlocked.", 0)):
			typewrite(actionprint)
			

		elif compare("open", "drawer", "The drawer was not locked.\n You open it and find a key in there.\n Are you going to take the key?", 0):
			typewrite(actionprint)
			drawer()

		elif (compare("open", "door", "You are trying to open the door, but it seems to be locked!", 0) or compare("go", "door", "You are trying to open the door, but it seems to be locked!", 0)) and haveKey1 == 0:
			typewrite(actionprint)
			

		elif (compare("open", "window", "You are trying to open the window, but it's fixed, no way to open it!", 0) or compare("go", "door", "You are trying to open the door, but it seems to be locked!", 0)):
			typewrite(actionprint)
			

		elif (compare("open", "door", "The door opened!",0) or compare("go", "door", "The door opened!",0)) and haveKey1 == 1 :
			typewrite(actionprint)
			typewrite("You step through the open door."+"\n")
			corridor1()

		elif "scream" in next_command.lower() :
			typewrite("You started to scream from the top of your lungs until you were out of air!" + "\n")
			typewrite("After you finished, you still can hear the ringing in your ears because of how loud you screamed." + "\n")
			typewrite("But suddenly you see something move in the dark!"),time.sleep(0.3),typewrite(" You startled something!" + "\n")
			typewrite("The creature leaps towards you from the shadows and you can't do anything!" + "\n")
			dead("A vampire jumped at you and sucked the blood out of you!")
		
		elif compare("look", "window", "You look out the window.\nIt is dark outside. All you can see is the wall of the castle and the \ntrees dancing a violent dance in the strong wind.",0):
			typewrite(actionprint)

		else:
			print "That is not a proper command. Please try again!" 


def corridor1():
	global been_to_corrdior
	if been_to_corrdior == 0 :
		typewrite("\nYou arrive at the end of a corridor."+"\n")
		time.sleep(0.3)
		typewrite("It is dimly lit, by torches all the way." + "\n")
		typewrite("You hear a big thunderclap and see the light of the lighining flashing at your feet on the floor through the window from outside."+"\n")
		typewrite("The corridor echoes with the sound of the thunderclap."),time.sleep(0.3),typewrite(" After that you can only hear the sounds of the burning torches and your own breathing."+"\n")
		typewrite("You take a deep cold breath and decide to find your way out of here."+"\n")
		been_to_corrdior = 1

	
	else:
		typewrite("You are back on the cold corridor..." + "\n")

	corridor_protocol()	


def corridor_protocol() :	
	while True:
		typewrite("Which way do you go?"+"\n")
		promptme()
		if "help" in next_command.lower():
			typewrite("The availble commands are:" + "\n")
			typewrite("Left" + "\n")
			typewrite("Back" + "\n")

		elif "left" in next_command.lower():
			typewrite("You decided to take the left turn."+"\n")
			if been_to_corrdior == 0 :
				typewrite("It is a long corridor and you are walking along with it."),time.sleep(0.2),typewrite("The only company is the echo of your steps on the cold stones." + "\n")
			door1()
			break
		#elif "right" in next_command.lower():
		#	typewrite("You decided to go right."+"\n")
		elif "back" in next_command.lower():
			typewrite("You decided to go back to the room."+"\n")
			room1()
		else :
			print "Can't decide which way to go?"
			
		
def drawer():
	
	global haveKey1
	while True:
		promptme()
		if "yes" in next_command.lower():
			typewrite("You took the key and closed the drawer back." +"\n")
			haveKey1 = 1
			break
		elif "no" in next_command.lower():
			typewrite("You close the drawer and leave the key behind." + "\n")
		else :
			print "Can't decide?"

def door1():

	if lock1_solved == 0 :
		typewrite("You arrive at a big stone door."),time.sleep(0.2),typewrite(" It seem to have a lock on it with ten numbers [ 0 - 9]." + "\n")
		typewrite("You are trying hard to read the text, but all you can read is that the lock needs three numbers,"),time.sleep(0.3),typewrite(" it might take a while to figure out." + "\n")
		
	else :
		typewrite("You are facing the stone door again." + "\n")
	stonedoor()

def stonedoor():
	while True :
		typewrite("What are you going to do?" + "\n")
		promptme()
		if "help" in next_command.lower():
			typewrite("The availble commands are:" + "\n")
			typewrite("Go" + "\n")
			#typewrite("Take" + "\n")
			typewrite("Open" + "\n")
		elif "back" in next_command.lower():
			typewrite("You decided to go back!"+"\n")
			corridor1()
		elif (compare("open", "door","You are trying to open the door, but the lock doesnt move. \n You decided to try open it!",0) or compare("open", "lock","You are trying to open the door, but the lock doesnt move. \n You decided to try open it!",0)) :
			lock1()

def lock1():
	global lock1_solved
	if lock1_solved == 0 :

		typewrite("This lock seems to be very old."),time.sleep(0.2),typewrite(" You even have to blow the dust off of it." + "\n")
		typewrite("You take a good look at the lock but there isn't anything else to do, than just enter the three numbers."),time.sleep(0.3),typewrite(" Let's hope for the best!" + "\n")
	else:
		typewrite("At the lock again" + "\n")
	lockmechanism(['6', '3', '7'])

def lockmechanism(code):
	global lock1_solved
	while True:
		try:
			typewrite("What are the 3 numbers you want to try?"+ "\n")
			typewrite("Or would you rather leave?" + "\n")
			promptme()

			numbers_equal = 0
			#this takes the userinput splits it up at the spaces into a list of "usercode"
			usercode = next_command.split(' ')

			
			# This line of code checks how many of the user input are equal to the "secret" code.
			#thank you meatypocket and Veedrac.
			for usercode_number, code_number in zip(usercode, code):
				if usercode_number == code_number:
					numbers_equal +=1
			
			if len(usercode) != 3:
				typewritefast("I said enter 3 numbers! %s is not 3 numbers. Please enter 3 numbers or leave the lock." % next_command + "\n")

			elif numbers_equal == 3 :
				#In grey you can see my original concept which did the job, but at the same time, it sucked.
				#usercode[0] == code[0] and usercode[1] == code[1] and usercode[2] == code[2] :
				lock1_solved = 1
				typewrite("You hear 3 slow clicks. You entered the right numbers!" + "\n")
				typewrite("The door slowly opens up and you step through it." + "\n")
				room2()
			
			elif numbers_equal == 2 :
				#(usercode[0] == code[0] and usercode[1] == code[1] and usercode[2] != code[2]) or (usercode[0] == code[0] and usercode[1] != code[1] and usercode[2] == code[2]) or (usercode[0] != code[0] and usercode[1] == code[1] and usercode[2] == code[2]) :
				typewrite("This time you heard two clicks behind the door, and silence. It's definitely something! But the door still doesn't move." + "\n")
		
			elif numbers_equal == 1 :
				#(usercode[0] == code[0] and usercode[1] != code[1] and usercode[2] != code[2]) or (usercode[0] != code[0] and usercode[1] == code[1] and usercode[2] != code[2]) or (usercode[0] != code[0] and usercode[1] != code[1] and usercode[2] == code[2]) :
				typewrite("You hear a click behind the door, but then nothing. And the door didn't move." + "\n")
		

			elif "leave" in next_command.lower():
				typewrite("You decieded to go back!" + "\n")
				corridor1()
			else:
				typewrite("You pressed the three numbers, but nothing just silence."),time.sleep(0.2),typewrite(" Probably the wrong numbers." + "\n")
		except IndexError:
			typewrite("Index Error.")



def room2():
	monster("Zombie", 55, 4 )
	typewrite("You find yourself in a fairly small room." + "\n")
	typewrite("Suddenly you realize that something is moving in the darker corner of the room..." + "\n")
	typewrite("As it comes to light, you see that its some kind of monster and he is blocking the way to the door on the opposite end!" + "\n")

	encounter()

def room3():
	typewrite("You defeated the enemy and went out the door!" + "\n")
	typewrite("You find yourself outside at the front of the caslte!" + "\n")
	typewrite("Cold rain falls on your face and the wind is blowing your hair." + "\n")
	typewrite("Finally you got away! The game is over." + "\n")
	print ""
	time.sleep(3)
	typewriteslow("Or is it?" + "\n")
	print""
	exit("Congratulations! You won!" + "\n")



def monster(name, HP, AD):
	global monster_name
	global monster_HP
	global monster_AD

	monster_name = name
	monster_HP = HP
	monster_AD = AD


#Encounter gives options for actions
def encounter():
	typewrite("You are facing a %s!" % monster_name + "\n" )
	typewrite("What are you gonna do?" + "\n")
	typewrite("Fight or flee?" + "\n")
	monster_alive = True
	while monster_alive == True:
		promptme()

		if "help" in next_command.lower():
			typewrite("The availble commands are:" + "\n")
			typewrite("Fight" + "\n")
			typewrite("Flee" + "\n")

		elif "fight" in next_command.lower():
			fight()
			room3()
		elif "flee" in next_command.lower():
			corridor1()
		else :
			print "That's not good!"

#It is the calculator to tell what attack will the monster perform. 
#I could make that different monsters have different attacks, and if I will expand my code in the future I will add it.
#Probably will happen, since I had lots of fun writing this short game.
def run(location) :
	run_chance = random.randrange(0,11)
	if run_chance > 5:
		typewrite("You could run away!" + "\n")
		location()
	else:
		typewrite("The %s didn't let you get away!" % monster_name + "\n" )
		monster_damage()
		if player_HP  <= 0 :
			dead("The %s has killed you!" % monster_name + "\n")

def monster_attack_calculator():
	global monster_AD
	global player_HP
	#getting a random number in the range of 1 to 15.
	hitchance = random.randrange(1,16)
	if hitchance < 5 :
		return "hit"
	elif hitchance >= 4 and hitchance <= 12:
		return "slash"
	else :
		return "missed"

#This is a monster damage calculator where in this case we calculate the damage output of the monster(s) 
#It could be even more modular, like a different function for different attacks (which would make reusabilty a bliss) if I had more monsters,
#But since its the last day of the assignment I will have to leave it at that.
def monster_damage():
	global	monster_name
	global monster_AD
	global	player_HP
	#The formulas:
	#slash = monster_AD * random.uniform(3.0,5.0)
	#hit = monster_AD * random.uniform(0.7,1.5)
	missed = 0

	#setting the attack to the result of attack calculator.
	attack = monster_attack_calculator()
	if attack == "hit" :
		#calculating the damage of the monster
		hit = monster_AD * random.uniform(0.7,1.5)
		#converting the long ass float into a string with a number with 2 decimals.
		a = "%.2f" % hit
		#converting back the shorter string to usable numbers
		hitdamage = decimal.Decimal(a)
		typewritefast("The %s has hit you for %s damage!" % (monster_name, hitdamage) + "\n" )
		player_HP = player_HP - hitdamage
		typewrite("You have %s health left!" % player_HP + "\n")
		return player_HP
		
		#same thing happens here as it happened in the hit case
	elif attack == "slash":
		slash = monster_AD * random.uniform(1.5,2.5)
		a = "%.2f" % slash
		slashdamage = decimal.Decimal(a)
		typewritefast("The %s has slashed you for %s damage!" % (monster_name, slashdamage) + "\n" )
		player_HP = player_HP - slashdamage
		typewrite("You have %s health left!" % player_HP + "\n")
		return player_HP

	elif attack == "missed" :
		typewritefast("The %s missed the attack!" % monster_name + "\n" )
		player_HP = player_HP - missed
		typewrite("You have %s health left!" % player_HP + "\n")
		return player_HP

	else:
		print "something is wrong need recoding."

# The fight module where action is taken and then the fight happens pretty much., 
def fight():
	global monster_name
	global monster_HP
	global monster_AD
	global player_AD
	global player_HP

	#kick = player_AD * random.uniform(1, 1.7)
	#hit = player_AD * random.uniform(0.5,1)
	
	typewritefast("You decided to fight!" + "\n")
	typewritefast("What action do you want to take?" + "\n")

	game_on = True
	while game_on == True:
		promptme()
		
		if "help" in next_command.lower():
			typewrite("The availble commands are:" + "\n")
			typewrite("Kick" + "\n")
			typewrite("Hit" + "\n")
			typewrite("Run" + "\n")

		elif "kick" in next_command.lower():
			kick = player_AD * random.uniform(1.1, 2)
			a = "%.2f" % kick
			kickdamage = decimal.Decimal(a)
			typewritefast("You kicked the %s" % monster_name + "\n")
			monster_HP = monster_HP - kickdamage
			typewritefast("%s took %s damage!" % (monster_name, kickdamage) + "\n")
			typewritefast("%s has %s hp left!" % (monster_name, monster_HP) + "\n")
			#I probably could put this if into a function like "deadcheck()"
			if monster_HP <= 0 :
				typewritefast("Congratulation, you defeated the %s!" % monster_name + "\n")
				return False
				game_on = False	
			else :
				monster_damage()
				#Game created by Peter Szabo. 2013.08.13
				if player_HP  <= 0 :
					dead("The %s has killed you!" % monster_name + "\n")

		elif "hit" in next_command.lower():
			hit = player_AD * random.uniform(0.5,1)
			a = "%.2f" % hit
			hitdamage = decimal.Decimal(a)
			typewritefast("You hit the %s" % monster_name +"\n")
			monster_HP = monster_HP - hitdamage
			typewritefast("%s took %s damage!" % (monster_name, hitdamage) + "\n")
			typewritefast("%s has %s hp left!" % (monster_name, monster_HP) + "\n")
			if monster_HP <= 0 :
				typewritefast("Congratulation, you defeated the %s!" % monster_name + "\n")
				return False
				game_on = False	
			else :
				monster_damage()
				if player_HP  <= 0 :
					dead("The %s has killed you!" % monster_name + "\n")
		elif "run" in next_command.lower():
			run(corridor1)

		



#function for being dead. gives a choice to restart or quit the game.
def dead(reason):
	time.sleep(0.3)
	typewritefast("You died!" + "\n")
	print "\n"
	typewrite(reason + "\n")
	typewritefast("Would you like to start the game again or exit the game?" + "\n")


	while True:
		promptme()
		if "start" in next_command.lower():
			typewritefast("You decided to start the game again!  Have fun!" +" \n")
			start()

		elif "exit" in next_command.lower():
			exit("You decided to exit the game! Hope you had fun!" +"\n")
		else :
			typewrite("You only have that 2 options! Pick one!" + "\n")


start()

