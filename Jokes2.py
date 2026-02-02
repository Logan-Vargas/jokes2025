# make this performance task ready for submission
# To give the user a fun experience hearing knock knock jokes
#The purpose is going to be able to create jokes

def commence_the_knock_knock(joke_value):
    input("Knock Knock")
    input(joke_tag[joke_value])
    print(joke_punch[joke_value])
    want_joke = input("Do you want to hear another joke or are you finished? ")
    return want_joke


system_on = 1
joke_tag = []
joke_punch = []

while system_on == 1:

    init_input = str(input("Welcome to the joke creation tool! Start by naming the joke that you want to make, or type 'end' to proceed to the next phase. "))
    if init_input.lower() == 'end':
        break
    else:
        joke_tag.append(init_input)
        punch_input = str(input("Great name! Now, what will your punchline be when the user asks 'who?' "))
        joke_punch.append(punch_input)
        print(joke_tag)
        print(joke_punch)
        print('Cool!')

while system_on == 1:
    print("Your friend made a slew of jokes for you to laugh at ")
    print('The names of the jokes are as follows:')
    print(joke_tag)
    friend_input = str(input("Which joke do you want? Type 'end' to proceed to the next phase: "))
    if friend_input.lower == 'end':
        break
    else:
        temp1 = -1
        for x in joke_tag:
            temp1 += 1
            if friend_input.lower() ==  x.lower():
                commence_the_knock_knock(temp1)
                heard_joke = 1
        if heard_joke == 0:
                print("No match, try again!")
