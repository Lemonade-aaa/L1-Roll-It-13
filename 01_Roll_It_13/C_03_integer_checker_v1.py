
error = "Please enter an integer that is more or equal to 13."

while True:
    try:
        game_goal = int(input("What is the end goal of this game?"))

        if game_goal < 13:
            print(error)
        else:
            print(f"Game goal:{game_goal}")
            break

    except ValueError:
        print(error)

