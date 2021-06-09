available_exits = ["north", "south", "east", "west"]

chosen_exit = ""
while chosen_exit.casefold() not in available_exits:
    chosen_exit = input("please choose direction: ")
    if chosen_exit.casefold() == "quit":
        print("game over")
        break

print("arent you glad you got out of there")
