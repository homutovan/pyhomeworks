def say_hello():
    print("Hello, World!")

# person = "World"

def say_hello_person(action="greet"):

    global person
    person = "Erica"

    print(f"In func: {person}")
    if action == "greet":
        return f"Hello, {person}!"
    elif action =="bye" :
        return f"Goodbye, {person}!"
    else:
        return f"Unknown action {action}"

# result = say_hello_person("errgerg")

def add(a, b):
    return  a + b

def div(a: int, b: int) -> float | None:
    if b == 0:
        print("division by zero")
        return
    
    elif type(b) != int or type(a) != int:
        print("unsupported types!")
        return
    
    return a / b

print(div(10, 0))


