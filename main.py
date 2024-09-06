
player_name= input("Welcome to GC mini golf! What is your name? ")
print (f"Hi, {player_name}! Would you like to play 3 or 6 holes today?")
holes= input()
holes= int(holes)

if holes== 3:
    hole1= input("How many putts for Hole 1? (par is 3) ")
    hole1= int(hole1)
    hole2= input("How many putts for Hole 2? (par is 3) ")
    hole2= int(hole2)
    hole3= input("How many putts for Hole 3? (par is 3) ")
    hole3= int(hole3)

    par= hole1+hole2+hole3

    par= int(par)

    score= par - 9

    if score>=0:
        print(f"Nice try, {player_name}, your total score was +{score}")
    elif score==0:
        print(f"Good game, {player_name}, your score was 0")
    elif score<=0:
        print(f"Great job, {player_name}, your score was -{score}")

elif holes== 6:
    hole1 = input("How many putts for Hole 1? (par is 3) ")
    hole1 = int(hole1)
    hole2 = input("How many putts for Hole 2? (par is 3) ")
    hole2 = int(hole2)
    hole3 = input("How many putts for Hole 3? (par is 3) ")
    hole3 = int(hole3)
    hole4 = input("How many putts for Hole 4? (par is 3) ")
    hole4 = int(hole4)
    hole5 = input("How many putts for Hole 5? (par is 3) ")
    hole5= int(hole5)
    hole6 = input("How many putts for Hole 6? (par is 3) ")
    hole6= int (hole6)

    par= hole1 + hole2 + hole3 + hole4 + hole5 + hole6
    print(par)
    par= int(par)

    score= par - 18

     if score>=0:
        print(f"Nice try, {player_name}, your total score was +{score}")
     elif score==0:
        print(f"Good game, {player_name}, your score was 0")
     elif score<=0:
        print(f"Great job, {player_name}, your score was -{score}")

else: print ("Sorry, we don't have that course. please try again.")