p1 = input("player1,enter choice rock, paper or scissors: ").lower()
p2 = input("player2,enter choice rock, paper or scissors: ").lower()
if p1 == p2:
    print("It's a tie!")
elif p1 == 'rock':
    if p2 == 'scissors':
        print("p1 wins!")
    else:
        print("p2 wins!")
elif p1 == 'scissors':
    if p2 == 'paper':
        print("p1 win!")
    else:
        print("p2 wins!")
elif p1 == 'paper':
    if p2 == 'rock':
        print("p1 wins!")
    else:
        print("p2 win!")
else:
    print("Invalid input! You have not entered rock, paper or scissors, try again.")