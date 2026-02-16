import random
username = input("What you you like to be referred as? ")


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


def make_statement(statement, decoration):
    """Adds emoji / additional characters to the start and end of headings"""

    ends = decoration * 3
    print(f"\n{ends} {statement} {ends}")

#main start here...


# At the start of the game, the computer / user score are both zero
comp_score = 0
user_score = 0
rounds_played = 0

game_goal = int(input("Game Goal: "))

# play multiple rounds until a winner has been found
while comp_score < game_goal and user_score < game_goal:

    rounds_played += 1

    # Start of round loop
    make_statement(f"Round {rounds_played}" , "🎲")

    # Roll the dice for the user and note if they got a double
    initial_user = initial_points(f"{username}")
    initial_comp = initial_points("Comp")

    # Retrieve user points (first item returned from function)
    user_points = initial_user[0]
    comp_points = initial_comp[0]

    double_user = initial_user[1]

    # Let the user know if they qualify for double points
    if double_user == "yes":
        print("Congratulations, If you are successful in victory you shall gain twice the amount of points.")

    # assume user goes first...
    first = f"{username}"
    second = "Computer"
    player_1_points = user_points
    player_2_points = comp_points

    if user_points < comp_points:
        print("You shall be first as you initial roll was less than the machines\n")

    # if the user and computer has fewer points, the user is player 1...
    elif user_points == comp_points:
        print("The Initial rolls were equal so you the user shall start")

    # If the computer has fewer points, switch the computer to 'player 1'
    else:
        player_1_points, player_2_points = player_2_points, player_1_points
        first, second = second, first

    # Loop until we have a winner
    while player_1_points < 13 and player_2_points < 13:
        print()
        input("Please press <enter> to continue this round\n")

        # first person rolls the die and score is updated
        player_1_roll = random.randint(1, 6)
        player_1_points += player_1_roll

        print(f"{first}: Rolled a {player_1_roll} - has {player_1_points} points.")

        # if the first person's score is over 13, end the round
        if player_1_points >= 13:
            break

        # second person rolls the die (and score is updated)
        player_2_roll = random.randint(1, 6)
        player_2_points += player_2_roll

        print(f"{second}: Rolled a {player_2_roll} - has {player_2_points} points.")

        print(f"{first}: {player_1_points}  | {second} {player_2_points}")

    # print("Rounds completion.")

    # switch the user and computer points if the computer went first
    user_points = player_1_points
    comp_points = player_2_points

    # work out who won...
    if first == "computer":
        user_points, comp_points = comp_points, user_points

    if user_points > comp_points:
        winner = f"{username}"
        loser = "comp"
        comp_points = 0
    else:
        winner = "computer"
        loser = f"{username}"
        user_points = 0

    round_feedback = f"{winner} has claimed victory. As {loser} has lost, their points will be reset to zero"

    # double user points if eligible
    if winner == "user" and double_user == "yes":
        user_points = user_points * 2

    # Output round results
    make_statement("Round Results", "=")
    print(f"{username} Points: {user_points}  |  Computer {comp_points}")
    print(round_feedback)
    print()

    # Outside rounds loop -  Update score with round points, only add points to the score of the
    comp_score += comp_points
    user_score += user_points

    # show overall scores (add this to rounds loop)
    print("*** Game Update ***")    # replace with call to statement generator
    print(f"{username} score: {user_score}  |  Computer score: {comp_score}")


# end of entire game, output final results.

make_statement("Game over" , "🏁")

print()
if user_score > comp_score:
    print(f"{username} won")   # replace this with statement generator call
else:
    print("The computer won")
