def get_age():
    age=input("How old are you?")
    return int(age)
def get_name():
    name=input("Anounce your name!")
    return name
user_age=get_age()
user_name=get_name()
print(f"Hi{user_name},I now know that you are{user_age} years old!")
