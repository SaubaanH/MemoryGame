"""
Purpose: The purpose of MatchingGame.py is to use PG Zero to create the classing Matching Card game. It uses various algorythms and modules needed to create a interactive game where it registers clicks to flip cards on the gameboard in hopes to get matching cards. The main purpose of creating the code is for an assignment but can also be used for leisure purposes  

Author: Saubaan Hasan
Creation Date: 09/06/2021
"""
#Imports the modules needed throughout the code
import pgzrun 
import random
import time


#Sets the dimentions of the gameboard
WIDTH = 345
HEIGHT = 460


#Size and location of buttons
cards = [Rect((10, 10), (100, 100)), Rect((120, 10), (100, 100)), 
Rect((230, 10), (100, 100)), Rect((10, 120), (100, 100)), 
Rect((120, 120), (100, 100)), Rect((230, 120), (100, 100)), 
Rect((10, 230), (100, 100)), Rect((120, 230), (100, 100)), 
Rect((230, 230), (100, 100)), Rect((10, 345), (100, 100)), 
Rect((120, 345), (100, 100)), Rect((230, 345), (100, 100))] 
#Color of Buttons
cardColors = (255, 0, 0)
#Timer for buttons
cardsPressed = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#Numbers for Cards
cardNumbs = ["1", "2", "3", "4", "5", "6", "1", "2", "3", "4", "5", "6"]
#Position of the numbers
numberPos = [(10, 10), (120, 10), (230, 10), (10, 120), (120, 120), (230, 120), (10, 230), (120, 230), (230, 230), (10, 345), (120, 345), (230, 345)]
#Initiates a Counter
counter = 0
#Initiates a Counter to check the number out of the pair that have been chosen (ex: 0/2, 1/2, 2/2)
matchingCounter = 0
#List of the current numbers that have been chosen including "-1" in the beginngin to avoid an error
currentNum = [-1]
#List of the clicked numbers that have been chosen
listOfCardClicked = []
#List of the matched cards that have been already matched
matching = []
#Value used to check if the card is currently being used (clicked)
truth1 = 0
truth2 = 0
truth3 = 0
truth4 = 0
truth5 = 0
truth6 = 0
truth7 = 0
truth8 = 0
truth9 = 0
truth10 = 0
truth11 = 0
truth12 = 0

#Shuffles the Deck
random.shuffle(cardNumbs) 

# Gives each button a variable to help check if it needs to be disabled or not
butt0 = 0
butt1 = 0
butt2 = 0
butt3 = 0
butt4 = 0
butt5 = 0
butt6 = 0
butt7 = 0
butt8 = 0
butt9 = 0
butt10 = 0
butt11 = 0

# Fills the screen with black, then handles the printing of numbers, cards and winner message to the gameboard
def draw():

  global matching, listOfCardClicked,matchingCounter

  #Fills the game window in black
  screen.fill((0,0,0))

  #Cycles through cards 
  for i in range (0, len(cards)):

    #checks the inputted button number to check if the given card has been clicked
    if cardsPressed[i] > 0:
      screen.draw.rect(cards[i], cardColors) #Prints a hollow rectangle as the "flipped card"
      screen.draw.text(cardNumbs[i], numberPos[i], color="white", fontsize=19) #Prints the randomized number under the given rectangle
    else:
      screen.draw.filled_rect(cards[i], cardColors) #if the card hasnt been clicked, this prints a filled rectangle at the given location

  #Covers the matched cards with black to appear disabled
  for i in range (0, len(matching)):
    screen.draw.filled_rect(cards[matching[i]], (0,0,0))

  #If all 12 buttons have been matched with one another, It prints the winning message 
  if len(matching) == 12:
    screen.draw.text("!WINNER!", (140,210), color="yellow", fontsize=19)


# Constantly runs so that it can properly keep track of the time and checks when the timer starts and finishes
def update(dt):
  
  #Calls all necessary variables needed in the function
  global cardsPressed, counter, listOfCardClicked,matching, matchingCounter,currentNum,truth1,truth2,truth3,truth4,truth5,truth6,truth7,truth8,truth9,truth10,truth11,truth12
  
  #Checks if 2 cards have been chosen so that the timer can go down.
  if counter % 2 == 0: 
    for i in range(0, len(cards)):
      if cardsPressed[i] > 0:
        cardsPressed[i] -= 1

  #Checks if 2 cards have NOT been chosen so that the timer won't go down until 2 cards have been chosen.
  else:
    for i in range(0, len(cards)):
      if cardsPressed[i] > 0:
        cardsPressed[i] -= 0
    
  #Goes through all 12 cards pressed timers to see if any of them are counting down to 0, and if they are it sets the respective value to 0 which is false or 1 which is true  
  for i in range (0, len(currentNum)):
    if cardsPressed[0] != 0:
      truth1 = 1
    else:
      truth1 = 0
    if cardsPressed[1] != 0:
      truth2 = 1
    else:
      truth2 = 0
    if cardsPressed[2] != 0:
      truth3 = 1
    else:
      truth3 = 0
    if cardsPressed[3] != 0:
      truth4 = 1
    else:
      truth4 = 0
    if cardsPressed[4] != 0:
      truth5 = 1
    else:
      truth5 = 0
    if cardsPressed[5] != 0:
      truth6 = 1
    else:
      truth6 = 0
    if cardsPressed[6] != 0:
      truth7 = 1
    else:
      truth7 = 0
    if cardsPressed[7] != 0:
      truth8 = 1
    else:
      truth8 = 0
    if cardsPressed[8] != 0:
      truth9 = 1
    else:
      truth9 = 0
    if cardsPressed[9] != 0:
      truth10 = 1
    else:
      truth10 = 0
    if cardsPressed[10] != 0:
      truth11 = 1
    else:
      truth11 = 0
    if cardsPressed[11] != 0:
      truth12 = 1
    else:
      truth12 = 0
  
# Handles the main algorythm to check for card matches 
def pressCard(num):

  #Calls all necessary variables needed in the function
  global cardsPressed,counter, listOfCardClicked, matching, butt0,butt1,butt2,butt3,butt4,butt5,butt6,butt7,butt8,butt9,butt10,butt11, matchingCounter,currentNum, truth1,truth2,truth3,truth4,truth5,truth6,truth7,truth8,truth9,truth10,truth11,truth12

  #Adds num to a list so that the current number can be refrenced when needed
  currentNum.append(num)

  #Cycles through cardsPressed to see if the previous number is still counting down, so that the timer for both cards expire at the same time. If there is not a count down happening, it sets the countdown to default value.  
  for i in range (0, len(currentNum)):
    if cardsPressed[currentNum[i]] != 0:
      cardsPressed[num] = cardsPressed[currentNum[i]]
    else:
      cardsPressed[num] = 120
      
  #Checks if the player has clicked more than 1 time and if the amout of times the player clicked is even (has a remainder of 0)
  if counter >=2  and counter % 2==0:

    #Checks if the 2 cards clicked have the same value but not the same exact card to determine if there is a matching card. 
    if cardNumbs[listOfCardClicked[-1]]==cardNumbs[listOfCardClicked[-2]] and listOfCardClicked[-2] != listOfCardClicked[-1]:
      
      #prints a message that 2 cards have been matched
      print('Matching!')

      #Adds the 2 matching cards to the matching list
      matching.append(listOfCardClicked[-1])
      matching.append(listOfCardClicked[-2])

      #cycles through the matching card list and assigning the buttons a deactivation value of 1, so that they wont be clicked again once matched
      for i in range (0, len(matching)):
        if matching[i] == 0:
          butt0 = 1
        if matching[i] == 1:
          butt1 = 1
        if matching[i] == 2:
          butt2 = 1
        if matching[i] == 3:
          butt3 = 1
        if matching[i] == 4:
          butt4 = 1
        if matching[i] == 5:
          butt5 = 1
        if matching[i] == 6:
          butt6 = 1
        if matching[i] == 7:
          butt7 = 1
        if matching[i] == 8:
          butt8 = 1
        if matching[i] == 9:
          butt9 = 1
        if matching[i] == 10:
          butt10 = 1
        if matching[i] == 11:
          butt11 = 1

  #Checks if the conditions are met to reset the matching counter 
  if counter !=0 and matchingCounter == 2:
    if counter%matchingCounter == 0:    
      matchingCounter = 0

# Registers the mouse clicks and only opperates when less than 2 buttons have been pressed
def on_mouse_up(pos, button):

  #Calls all necessary variables needed in the function
  global counter, listOfCardClicked,butt0,butt1,butt2,butt3,butt4,butt5,butt6,butt7,butt8,butt9,butt10,butt11, matchingCounter , truth1,truth2,truth3,truth4,truth5,truth6,truth7,truth8,truth9,truth10,truth11,truth12

  #checks if there are 2 or less cards clicked which have their timers ticking down so that if there are more than 2, it disables all the other buttons until the timers have run out for the cards
  if truth1+truth2+truth3+truth4+truth5+truth6+truth7+truth8+truth9+truth10+truth11+truth12 >= 0 and truth1+truth2+truth3+truth4+truth5+truth6+truth7+truth8+truth9+truth10+truth11+truth12 <= 1:
    
    #Checks if there aren't 2 cards currently chosen 
    if matchingCounter !=2:
      
      #Checks if button 0 is active
      if butt0 == 0:
        #If button is clicked, in changes the values of counter, matchingCounter. It also adds the button number to a list and calls the pressCard Function
        if cards[0].collidepoint(pos):
          counter += 1
          matchingCounter += 1
          listOfCardClicked.append(0)
          pressCard(0)
      
      #Checks if button 1 is active
      if butt1 == 0:
        #If button is clicked, in changes the values of counter, matchingCounter. It also adds the button number to a list and calls the pressCard Function        
        if cards[1].collidepoint(pos):
          counter += 1
          matchingCounter += 1
          listOfCardClicked.append(1)
          pressCard(1)

      #Checks if button 2 is active
      if butt2 == 0:
        #If button is clicked, in changes the values of counter, matchingCounter. It also adds the button number to a list and calls the pressCard Function
        if cards[2].collidepoint(pos):
          counter += 1
          matchingCounter += 1
          listOfCardClicked.append(2)
          pressCard(2)

      #Checks if button 3 is active
      if butt3 == 0:
        #If button is clicked, in changes the values of counter, matchingCounter. It also adds the button number to a list and calls the pressCard Function
        if cards[3].collidepoint(pos):
            counter += 1
            matchingCounter += 1
            listOfCardClicked.append(3)
            pressCard(3)

      #Checks if button 4 is active
      if butt4 == 0:
        #If button is clicked, in changes the values of counter, matchingCounter. It also adds the button number to a list and calls the pressCard Function
        if cards[4].collidepoint(pos):
            counter += 1
            matchingCounter += 1
            listOfCardClicked.append(4)
            pressCard(4)

      #Checks if button 5 is active
      if butt5 == 0:
        #If button is clicked, in changes the values of counter, matchingCounter. It also adds the button number to a list and calls the pressCard Function
        if cards[5].collidepoint(pos):
            counter += 1
            matchingCounter += 1
            listOfCardClicked.append(5)
            pressCard(5)

      #Checks if button 6 is active
      if butt6 == 0:
        #If button is clicked, in changes the values of counter, matchingCounter. It also adds the button number to a list and calls the pressCard Function
        if cards[6].collidepoint(pos):
            counter += 1
            matchingCounter += 1
            listOfCardClicked.append(6)
            pressCard(6)

      #Checks if button 7 is active
      if butt7 == 0:
        #If button is clicked, in changes the values of counter, matchingCounter. It also adds the button number to a list and calls the pressCard Function
        if cards[7].collidepoint(pos):
            counter += 1
            matchingCounter += 1
            listOfCardClicked.append(7)
            pressCard(7)

      #Checks if button 8 is active
      if butt8 == 0:
        #If button is clicked, in changes the values of counter, matchingCounter. It also adds the button number to a list and calls the pressCard Function
        if cards[8].collidepoint(pos):
            counter += 1
            matchingCounter += 1
            listOfCardClicked.append(8)
            pressCard(8)

      #Checks if button 9 is active
      if butt9 == 0:
        #If button is clicked, in changes the values of counter, matchingCounter. It also adds the button number to a list and calls the pressCard Function
        if cards[9].collidepoint(pos):
            counter += 1
            matchingCounter += 1
            listOfCardClicked.append(9)
            pressCard(9)

      #Checks if button 10 is active
      if butt10 == 0:
        #If button is clicked, in changes the values of counter, matchingCounter. It also adds the button number to a list and calls the pressCard Function
        if cards[10].collidepoint(pos):
            counter += 1
            matchingCounter += 1
            listOfCardClicked.append(10)
            pressCard(10)

      #Checks if button 11 is active
      if butt11 == 0:
        #If button is clicked, in changes the values of counter, matchingCounter. It also adds the button number to a list and calls the pressCard Function
        if cards[11].collidepoint(pos):
            counter += 1
            matchingCounter += 1
            listOfCardClicked.append(11)
            pressCard(11)
pgzrun.go()


