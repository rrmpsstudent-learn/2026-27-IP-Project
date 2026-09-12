grid = [["A1","A2","A3"],["B1","B2","B3"],["C1","C2","C3"]]

def grid_creator():
    print("------------------")
    for i in grid:
        for j in i:
            print(f"| {j} |", end = "")
        print("\n------------------")

init_input = input("Enter your symbol(O/X): ")

grid_creator()

print("Enter the block you want to place your symbol at(With correct spelling, for eg - A2): \n")

if init_input == "X":
    user_symbol = "X"
else:
    user_symbol = "O"


choice_logs = list()
#0 means turn of user
chance_counter = 0


def combo_checker():
    for i in grid:
        if i.count("X") == 3 or i.count("O") == 3:
            return True
        else:
            continue


while(chance_counter <= 1 and not combo_checker()):
    if combo_checker():
            print(f"Player {user_symbol} Wins!!")
    choice = input(f"Player {chance_counter + 1} turn: ")
    choice_logs.append(choice.capitalize())
    #choice_str = choice.split(" ")
    choice_list = list()
    if choice.upper() == "QUIT":
        print("Thank you for playing")
        break
    elif choice.upper() == "SHOW --LOGS":
        print(choice_logs)
    else:
        for i in choice:
            choice_list.append(i)

        mapping = {'A':0,'B':1,'C':2}

        
    
        try:
            grid[mapping[choice_list[0]]][int(choice_list[1]) - 1] = f"{user_symbol}"
            grid_creator()

            print("\n" * 5)

            if chance_counter == 0:
                chance_counter += 1
            else:
                chance_counter -= 1

            if chance_counter == 1:
                user_symbol = "O"
            else:
                user_symbol = "X"
        except Exception as e:
            print("That didn't work! Please retry")


