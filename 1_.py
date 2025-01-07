
# functions are ways to wrap your code
# into reuseable units

#How you define a function
#Only define the function ONCE
#Whatever I pass inside the parenthesis
#It is called a parameter
#Parameter = placeholder for future information
# def sayHello(name,age,address):
#     print(f"Say hello {name}")
#     print(f"Hello Governor, your address is {address}")
#     print(f"Welcome back {name}")
#     print(f"Your age is {age}")

#once you define a function
#you must call or invoke the function
# when i pass in information into the called function
#it is called an arguement
#sayHello("Evins",30,"345 north lawndale ave")
#sayHello("Devin",69,)
#sayHello("Lara",86,)

# def determineElegibility(age):
#     #if your age is over 18, you can vote,
#     #otherwise you can't
#     if age >= 18:
#         print("You can vote")
#     else:
#         print("You cannot vote yet.")

# determineElegibility(12)
# determineElegibility(15)
# determineElegibility(19)

# def willYouGraduate(gpa,credits,SAT):
#     #gpa: Number float variable
#     #credits: Number variable
#     #SAT: Boolean variable
#     if (gpa == 3.0) and (credits >= 28) and (SAT == True):
#         print("You can graduate! Congrats!")
#     elif(gpa < 3.0) or (credits > 28) or (SAT != True):
#         print("You are not elegible to graduate.")
#     else:
#         print("Speak to your counselor.")
    
# willYouGraduate(2.8,30,True)
# willYouGraduate(0.2,14,False)
# willYouGraduate(4.0,30,True)

# return = statment used to end a function
#          and send a result back to the caller

# def add(x, y):
#     z = x + y
#     return z

# def subtract(x, y):
#     z = x - y
#     return z

# def multiply(x, y):
#     z = x * y
#     return z

# def divide(x,y):
#     z = x/y
#     return z

# print(add(1, 2))
# print(subtract(1, 2))
# print(multiply(1, 2))
# print(divide(1, 2))

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("spongebob", "squarepants")

print(full_name)