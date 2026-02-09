
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

# Main routine

want_instructions = yes_no("Would you like to see the instructions?").lower()



if want_instructions == "yes":
    instructions()

print()
print("Program continues")