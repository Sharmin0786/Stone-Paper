import random

def play():
    player = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors \n ")
    computer = random.choice(['r', 'p', 's'])

    if player == computer:
        return 'It is a tie'


    if is_win(player, computer):
        return 'You won!'   
    
    if is_win(computer, player):
      return 'You lost'    


def is_win(user, opponent):
    
    if (user == 'r' and opponent =='s') or (user == 's' and opponent =='p') or (user == 'p' and opponent == 'r'): 
        return True

print(play())