def greet_students(name):
    print(f"Hello, {name}! Welcome to python class.")

greet_students("Greatness")
greet_students("John")

def introduce(name, age, profession):
    print(f"My name is {name}.")
    print(f"I am {age} years old.")
    print(f"I am a {profession}.")

introduce("Greatness", 25, "Software Engineer")

def greet(name="James"):
    print(f"Hello, {name}! Welcome to python class.")

greet()
greet("Greatness")