
# Function
def yes_no(question):

    """Checks user response to a question is yes or no (y/n), returns 'yes' or 'no'"""

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
           return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Answer yes or no..")


def instructions():
    """Print instructions"""

    print("""
***INSTRUCTIONS***

Partake in rolling the dice and attempt to win.
    """)


def int_check():
    """Checks users enter an integer more than/equal to 13"""

    error = "Please enter an integer that is more or equal to 13."

    while True:
        try:
            response = int(input("What is the intended end goal for this game?"))

            if response < 13:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

# Main routine

want_instructions = yes_no("Would you like to see the instructions?").lower()



if want_instructions == "yes":
    instructions()

print()
game_goal = int_check()
print(game_goal)
