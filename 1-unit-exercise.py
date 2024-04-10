# 1-unit-exercise 
# Author: Jordan Bindra
# Date: Monday March 4 2024 


# Create a function called translate
#    Accepts a string as parameter
#    From the parameter replace all 1 with 1️⃣
#    Also replace all pizza with 🍕
#    Return the result
def translate(usr_input):
    # Your block of code goes in here
    # Delete the pass and put in your own code
    return usr_input.replace("1", "1️⃣").replace("pizza", "🍕")


def main():
    # Get the user's input
    usr_input = input("What would you like to translate? ")
    # Use the translate function on the
    #    user's input
    print(translate(usr_input))


# Test cases
print(translate("Get 1 slice!"))
print(translate("I like pizza."))
main()


# Ask the user if they are done their pizza
user_reply = input("Are you done your pizza? ")

# If they answer yes, say 
# I'll take the plate, thanks 
if user_reply.strip("!.?.,").lower() == "yes":
    print("I'll take the plate, thanks. ")

# If they answer no, say 
# Take your time
elif user_reply.strip("!.?.,").lower() == "no":
    print("Take your time. ")
else: 
    print("sorry I didn't understand what you said.")



# Tell the user the total cost and ask for tip 
def main():
    dollars = dollars_to_float(input(" 5 dollars is your total "))
    percent = percent_to_float(input(" What much would you like to tip? "))
    tip = dollars * percent

    print(f"Leave ${round(tip, 2)}")


def dollars_to_float(d: str):
    # Converts string dollars to a decimal float
    #    Returns the result
    return float(d)


def percent_to_float(p):
    # Converts percent to a decimal float
    #    Returns the result
    return float(p) / 100


main() 

# After paying tell the user bye
print("Bye")
