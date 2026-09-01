# Welcome to the R.P.S. game.
# Rules are as follows:
# 1> Rock destroys scissors
# 2> Paper destroys Rock
# 3> Scissors destroys paper
# 4> Same symbols are cancelled out


import random


results = {0:"You Lose!!",1:"You Win!!",-1:"The game ended in a draw!"}
convention = {0:"Rock",1:"Paper",2:"Scissors"}
combinations = [[-1,0,1],[1,-1,0],[0,1,-1]]
bot_inputs = [0,1,2]

bot_choice = random.choice(bot_inputs)

print("0 : Rock","1 : Paper","2 : Scissors")
user_input = int(input("Enter the symbol you choose: "))
print(f"Bot chooses {convention[bot_choice]}")

result = combinations[user_input][bot_choice]
print(results[result])