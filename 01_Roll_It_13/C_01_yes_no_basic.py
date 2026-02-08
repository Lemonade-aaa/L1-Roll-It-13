

while True:
    want_instructions = input("Would you like to see the instructions?").lower()

    if want_instructions == "yes" or want_instructions == "y":
        print("You have responded with yes.")
        break
    elif want_instructions == "no" or want_instructions == "n":
        print("You have responded with no.")
        break
    else:
        print("Answer yes or no..")
        continue

print("We have completed the steps prior and are bring this to a close")