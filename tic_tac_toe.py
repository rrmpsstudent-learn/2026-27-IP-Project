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
    combo_helper_list = list()
    for i in grid:
        if i.count("X") == 3 or i.count("O") == 3:
            print("Game Over!!")
            return True
        else:
            continue

    if grid[0][0] == grid[1][0] == grid[2][0] != "":
        print("Game Over!!")
        return True
    if grid[0][1] == grid[1][1] == grid[2][1] != "":
        print("Game Over!!")
        return True
    if grid[0][2] == grid[1][2] == grid[2][2] != "":
        print("Game Over!!")
        return True
    if grid[0][0] == grid[1][1] == grid[2][2] != "":
        print("Game Over!!")
        return True
    if grid[0][2] == grid[1][1] == grid[2][0] != "":
        print("Game Over!!")
        return True

    # Gemini generated:
    # # 1. Check all 3 Rows
    # for row in grid:
    #     if row[0] == row[1] == row[2] != " ": # Ensures the cells aren't empty
    #         print("Game Over!!")
    #         return True

    # # 2. Check all 3 Columns
    # for col in range(3):
    #     if grid[0][col] == grid[1][col] == grid[2][col] != " ":
    #         print("Game Over!!")
    #         return True

    # # 3. Check Left-to-Right Diagonal
    # if grid[0][0] == grid[1][1] == grid[2][2] != " ":
    #     print("Game Over!!")
    #     return True

    # # 4. Check Right-to-Left Diagonal
    # if grid[0][2] == grid[1][1] == grid[2][0] != " ":
    #     print("Game Over!!")
    #     return True


mapping = {'A':0,'B':1,'C':2}
choice_list = list()

while(chance_counter <= 1 and not combo_checker()):
    if combo_checker():
            print(f"Player {user_symbol} Wins!!")


    if grid[mapping[choice_list[0].upper()]][int(choice_list[1]) - 1] in ["X","O"]:
        print("That spot is already taken! Try again.")
        continue


    choice = input(f"Player {chance_counter + 1} turn: ")
    choice_logs.append(choice.capitalize())
    #choice_str = choice.split(" ")
    
    if choice.upper() == "QUIT":
        print("Thank you for playing")
        break
    elif choice.upper() == "SHOW --LOGS":
        print(choice_logs)
    else:
        for i in choice:
            choice_list.append(i)

        
    
        try:
            grid[mapping[choice_list[0].upper()]][int(choice_list[1]) - 1] = f"{user_symbol}"
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


