# unit 2 activit
# JB
# Monday April 8 2024 

def greet(name): 
    return f"hello, {name}"

def ask_how_are_you(): 
    respone = input(" How are you today? ")
    return respone 

def ask_where_for_lunch(prompt):
    response = input(prompt)
    return response

def provide_lunch_options():
    print("Here are some lunch options:")
    print("Mcdonalds")
    print("A&W")
    print("Subway")

for _ in range(2):
    user_input = input("user name")
    print(greet(user_input))

user_feeling = ask_how_are_you()
if user_feeling.lower() in ["good", "fine"]: 
    print("That's great to hear!")

else: 
    print("I hope you feel better")

lunch_destination = ask_where_for_lunch("Where are you going for lunch? ")
if lunch_destination.lower() == "not sure":
    provide_lunch_options()

else:
    print("You are going to", lunch_destination)
    print("Good Choice!")



