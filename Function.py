# Lab 37.

# # Function to add two numbers
# def add(*num):
#     result = (1+2+3+4+8)
#     return result

# # print("Addition:", add(8,15))
# add(2,3,4,56,7,8,8,99)
# print()
    
# i = 0 

# # Functiom to subtract two numbers
# def subtract(a,b):
#     result = a - b
#     print(result)
#     return result

# print("Subtraction:", subtract(15,4))


# # Function to multiply to numbers
# def multiply(a,b):
#     result = a*b
#     return result
# print("Multiplication:", multiply(6,8))
# print(multiply(3,5))    


# # Function to divide two numbers
# def divide(a,b):
#     if b != 0:
#         result = a / b
#     else:
#         result = "Cannot divide by zero"
#     return result
# print("division:", divide(16,5)) 
    

#Lab 38.

# # Positional Arguments
# def greet(name,age):
#     print(f"hello {name}, you are {age} years old.")

# greet("Anshika", 23)    


# # Keyword Arguments
# def greet(name,age,hobbie):
#     print(f"Hello {name},you are {age} year old. And my hobbie is {hobbie}.")

# greet (hobbie = "Listening song", name = "Anshika", age = 23)

# # Default Arguments
# def greet(name, age=23):
#     print(f"Hello {name}, you are {age} years old.")

# greet("Anshika")  # Uses default age value
# greet("Nitya",22)  # Overrides default age value    



# #Variable Length Arguments
# def print_number(*args):
#     for number in args:
#         print(number)

# print_number(1,2,3,4,5,6,7,8,9)     


# # Keyword Variable length Argument(**kwargs)

# def print_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# print_info(name= "Kumar", profession="Engineer")
# print_info(country="India", population=1.4e9, capital="New Delhi")        


# Mixing Different Argument Types

# def mixed_arguments(a, b=2, *args, **kwargs):
#     print(f"a: {a}")
#     print(f"b: {b}")
#     print(f"args:", args)
#     print(f"kwargs:", kwargs)

# mixed_arguments(1,3,4,5,10,20, x=2,y=5)  



 
