# Joke Creation Tool (refactoring the bad performance task) - About 80% finished
# By Logan Vargas and Antonio Williams

system_on = True
joke_tag = []
joke_punch = []

def commence_the_knock_knock(joke_value):
    input("Knock Knock ")
    input(joke_tag[joke_value])
    print(joke_punch[joke_value])
    want_joke = input("Do you want to hear another joke or are you finished? Type 'end' to proceed to the next phase. ")
    return want_joke


# For as long as you want to make new jokes, then you can make as many as you want! The program will only stop looping after the user types in "end."
while system_on == True:

    init_input = str(input("Welcome to the joke creation tool! Start by naming the joke that you want to make, or type 'end' to proceed to the next phase. "))
    if init_input.lower() == "end":
        break
    else:
        joke_tag.append(init_input)
        punch_input = str(input("Great name! Now, what will your punchline be when the user asks 'who?' "))
        joke_punch.append(punch_input)
        print(joke_tag)
        print(joke_punch)
        print("Great joke!")

# Now, you can bring another person over to laugh at the jokes you've created! The program will display all of the jokes for you, and the user can select which one they want.
print("Your friend made a slew of jokes for you to laugh at!")
while system_on:

# Here, the program will display the names of the jokes, and will move on if none are created! The user can select which joke they want.
    print("The names of the jokes are as follows:")
    print(joke_tag)
    friend_input = str(input("Which joke do you want? Type 'end' to proceed to the next phase. "))
    if friend_input.lower() == "end":
        break
    else:
        temp1 = -1
        heard_joke = 0
        for x in joke_tag:
            temp1 += 1
            if friend_input.lower() == x.lower():
                end_early = commence_the_knock_knock(temp1)
                heard_joke = 1
                if end_early == "end":
                    heard_joke = 2
        if heard_joke == 0:
            print("No match, try again!")
        if heard_joke == 2:
            break

def final_phase():
    rate = int(input("Please rate our game 1-10! "))
final_score = int(rate * 10)
print(str(final_score) + " percent satisfaction rate")
friend = input("Would you recommend this game to a friend? ")
if friend == "yes" or friend == "maybe":
        print("Thanks, we appreciate it. ")
else:
    print("Sorry you did not enjoy it. ")
    