# Mcdobot
# Author: Jordan 
# 21 February 2024 


# Ask the user if they want fries with their meal 
user_reply = input("Would you like fries with your meal? ")

# If they answer yes, say 
# here's your meal with fries 
if user_reply.strip("!.?.,").lower() == "yes":
    print("Here's is your meal with fries. ")

# If they answer no, say 
# Here's is your meal without fries
elif user_reply.strip("!.?.,").lower() == "no":
    print("Here's is your meal without fries. ")
else: 
    print("sorry I didn't understand what you said.")
