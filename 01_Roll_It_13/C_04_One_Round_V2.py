import random


def initial_points(which_player):
    """Roll the dice twice and return the total/if double points apply"""
    double = "no"

    # Roll the dice for the user and note if they double
    roll_one = random.randint(1, 6)
    roll_two = random.randint(1, 6)

    if roll_one == roll_two:
        double = "yes"

    total = roll_one + roll_two
    print(f"{which_player} - Roll 1: {roll_one} \t| Roll 2: {roll_two} \t| Total: {total}")

    return total, double

#main start here...


# Roll the dice for the user and note if they got a double
initial_user = initial_points("User")
initial_comp = initial_points("Comp")



# Retrieve user points (first item returned from function)
user_points = initial_user[0]
comp_points = initial_comp[0]

double_user = initial_user[1]

# Let the user know if they qualify for double points
if double_user == "yes":
    print("Congratulations, If you are successful in victory you shall gain twice the amount of points.")

#assume user goes first...
first = "User"
second = "Computer"
player_1_points = user_points
player_2_points = comp_points

if user_points < comp_points:
    print("You shall be first as you initial roll was less than the machines\n")

elif user_points == comp_points:
    print("The Initial rolls were equal so you the user shall start")


else:
    player_1_points, player_2_points = player_2_points, player_1_points
    first, second = second, first


while player_1_points < 13 and player_2_points < 13:
    print()
    input("Please press <enter> to continue this round\n")


    player_1_roll = random.randint(1, 6)
    player_1_points += player_1_roll

    print(f"{first}: Rolled a {player_1_roll} - has {player_1_points} points.")



    if player_1_points >= 13:
        break

    player_2_roll = random.randint(1, 6)
    player_2_points += player_2_roll

    print(f"{second}: Rolled a {player_2_roll} - has {player_2_points} points.")

    print(f"{first}: {player_1_points}  | {second} {player_2_points}")

print("Rounds completion.")
