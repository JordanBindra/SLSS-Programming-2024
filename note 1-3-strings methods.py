# Methods - String Methods 
# Author: Jordan 
# 21 February 2024 

 # Ask the user what the weather is 
user_reply = input("what is the weather like? ")

# If they answer rainy, say 
# bring an umbrella 
if user_reply.strip("!.?.,").lower() == "rainy":
    print("Bring an umbrella!")
else: 
    print("sorry I didn't understnad what you said.")
