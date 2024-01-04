from getpass import getpass as input
#getpass in this case prevents each player from viewing each other's input value
print("Hey Hey Hey,welcome to the rock paper scissors extravaganza :)") 
print("Da Rulz- You are required to select either R,P or S for every single chance you get in the game after the other player has made a move unless you are the one to start the game, got it?")
print("")
print("Great,let's go :)")
player1=input("Go on player 1 don't be shy, choose between R,P or S for your first move")
print("great, now it is player two's turn")
print("")
print("")
player2=input("Player 2 you're up, show em how it's done sonn, choose between R,P or S ")
if player1=="R" and player2=="R":
  print("Oh darn it you guys tied, let's give it another go yeah?")
elif player1=="R" and player2=="P":
  print("Alright! Player 2 you crasheddd thisss!")
elif player1=="R" and player2=="S":
  print("Alright! Player 1 you crasheddd thisss!")
elif player1=="P" and player2=="P":
  print("Oh darn it you guys tied, let's give it another go yeah?")
elif player1=="P" and player2=="R":
 print("Alright! Player 1 you crasheddd thisss!")
elif player1=="P" and player2=="S":
 print("Alright! Player 2 you crasheddd thisss!")
elif player1=="S" and player2=="S":
   print("Oh darn it you guys tied, let's give it another go yeah?")
elif player1=="S" and player2=="R":
 print("Alright! Player 2 you crasheddd thisss!")
elif player1=="S" and player2=="P":
 print("Alright! Player 1 you crasheddd thisss!")
else:
  print("Invalid choice,please be sure to use the options given to you at the begining of the game")
  




  
