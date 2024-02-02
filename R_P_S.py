import random
l = ["rock","scissor","paper"]
'''
rock vs paper -> paper wins
rock vs scissor -> rock wins
paper vs scissor -> scissor wins
'''

while True:
    ccount = 0
    ucount = 0
    userchoice = int(input('''
  GAME START...!
  1- YES
  2- NO | EXIT
   '''))
    if userchoice == 1:
        for a in range(1,6):
            userInput = int(input('''
1- ROCK
2- SCISSOR
3- PAPER
'''))
            if userInput == 1:
                uchoice = "rock"
            elif userInput == 2:
                uchoice = "scissor"
            elif userInput == 3:
                uchoice = "paper"
            Comp_choice = random.choice(l)
            if Comp_choice==uchoice:
                print("Computer Value",Comp_choice)
                print("User Value",uchoice)
                print("Game Draw")
                ccount = ccount+1
                ucount = ucount+1
            elif (uchoice=="rock" and Comp_choice == "scissor") or ( uchoice=="paper" and Comp_choice=="rock") or (uchoice=="scissor" and Comp_choice=="paper"):
                print("YOU WIN")
                ucount = ucount+1
            else:
                print("Computer Value", Comp_choice)
                print("User Value", uchoice)
                print("Computer Win")
                ccount = ccount + 1
        if ucount==ccount:
            print("GAME DRAW")
            print("User Score",ucount)
            print("Computer Score",ccount)
        elif ucount > ccount:
            print(" YOU WIN THE GAME ")
            print("User Score", ucount)
            print("Computer Score", ccount)
        else:
            print("COMPUTER WIN THE GAME ")
            print("User Score", ucount)
            print("Computer Score", ccount)
    else:
        break