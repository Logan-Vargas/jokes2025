# Joke Creation Tool (refactoring a student's performance task)
# By Logan Vargas and Antonio Williams

system_on = True
joke_tag = []
joke_punch = []
# ____________________________________________________________________________________________________________________________________________________________________________

def commence_the_knock_knock(joke_value):
    input("Knock Knock! ")
    input(joke_tag[joke_value] + "... ")
    print(joke_punch[joke_value])
    want_joke = input("Do you want to hear another joke or are you finished? Type 'end' to proceed to the next phase, or simply press enter to continue. ")
    return want_joke

def check_for_knock_knocks(input):
    temp1 = -1
    heard_joke = 0
    for x in joke_tag:
        # temp1 simply keeps track of how many times the loop has run, and uses it as an input when the input matches the current entry that's being checked.
        temp1 += 1
        if input.lower() == x.lower():
            # If a match is found, then the knock knock joke begins and the 'heard_joke' value will change.
            end_early = commence_the_knock_knock(temp1)
            heard_joke = 1
            # 'heard_joke' being set to 2 is necessary for the return value.
            if end_early == "end":
                heard_joke = 2
    return heard_joke

def final_phase():
    rate = int(input("Please rate our program [1-10]! "))
    final_score = int(rate * 10)
    print(str(final_score) + " percent satisfaction rate!")

def recommendation():
    friend = input("Would you recommend this program to a friend [yes, maybe, no]? ")
    if friend == "yes" or friend == "maybe":
        print("Thanks, we appreciate it!")
    else:
        print("That's a shame.... We still hope you enjoyed your time!")
# _________________________________________________________________ < INPUT START! > ________________________________________________________________________________

# For as long as you want to make new jokes, you can do so! The program will only stop looping after the user types in "end."
while system_on == True:

# First, the program asks what name the user wants their next joke to be. Otherwise, you can type 'end' to move on (if you have a joke made already).
    init_input = str(input("Welcome to the joke creation tool! Start by naming the joke that you want to make, or type 'end' to proceed to the next phase. "))
    # Below is the check for the user submitting 'end' - The program doesn't proceed unless a joke has been made already!
    if init_input.lower() == "end":
        if len(joke_punch) > 0:
            break
        else:
            print("Woah! You need to make a joke first! You're no fun!")
    # Otherwise, the program will add the name that the user typed in to the 'joke_tag' list.
    else:
        joke_tag.append(init_input)
        # Then, the program will ask the user for another input, this time for the 'joke_punch' list.
        punch_input = str(input("Great name! Now, what will your punchline be when the user asks 'who?' "))
        joke_punch.append(punch_input)
        print(joke_tag)
        print(joke_punch)
        # The inputs have now been appended, and both lists will be used in tandom later in the program.
        print("Nice joke!")
    # Printed lines for aesthetic.
    print("_" * 80)
    print("")
print("_" * 80)
print("")
# |
# |
# v___________________________________________________________________________________________________________________________________________________________________________

# Now, you can bring another person over to laugh at the jokes you've created! The program will display all of the jokes for you, and the user can select which one they want.
print("Your friend made a slew of jokes for you to laugh at!")
while system_on:

# Here, the program will display the names of the jokes in the 'joke_tag' list! The user can select which joke they want.
    print("The names of the jokes are as follows:")
    print(joke_tag)
    # Similarly to the above segment, the program asks for an input here.
    friend_input = str(input("Which joke do you want? Type 'end' to proceed to the next phase, or type in the joke you want to listen to it! "))
    # If the user types end, the loop breaks and the program goes on to the 'rating' phase.
    if friend_input.lower() == "end":
        break
    else:
        # If anything else is typed in, then the program proceeds here.
        check_return = check_for_knock_knocks(friend_input)
        # If no match is found, then that means an invalid prompt was given, and the program will display as much in the terminal.
        if check_return == 0:
            print("No match, try again!")
        # If the end of the program is called for at the end of the function's input, then 'heard_joke' (and therefore 'check_return') will be set to 2. 
        # This breaks the above 'while' loop.
        if check_return == 2:
            break
    # Printed lines for aesthetic.
    print("_" * 80)
    print("")
print("_" * 80)
print("")
# |
# |
# v___________________________________________________________________________________________________________________________________________________________________________

# We've had our fun now! Now, these final 2 functions include the math we need for our performance task and let the user give a rating!
if system_on:
    final_phase()
    recommendation()
# _____________________________________________________________________________________________________
