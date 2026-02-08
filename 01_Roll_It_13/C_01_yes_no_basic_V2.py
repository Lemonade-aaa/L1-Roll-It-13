
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

# Main routine

want_instructions = yes_no("Would you like to see the instructions?").lower()
want_money = yes_no("Do you want some money")

print("You have completed the steps prior and thus bringing this to a close")