# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.


def greet():
    print("Hello")
    print("Hola!")
    print("Konnichiwa")

greet()



def greet_with_name(name):
    print(f"Hello {name}")

# Here "name" is the paramete of the data thats the used in the funciton. The actual value passed is called arguargument 

greet_with_name("rajat")

# Defining a function with multiple arguements

def greet_with(name, location):
    print(f"Hello {name}. Hows the weather in {location}")

greet_with("rajat", "Pune" )

# Call the fucntion greet_with using keyword arguements

greet_with(location = "pune", name = "Rajat")