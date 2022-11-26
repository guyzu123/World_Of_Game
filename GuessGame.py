import random
difficulty=1
def generate_number():
    secret_number = random.randint(0,difficulty)
    return secret_number
def get_gues_from_user():
    user_number=input("guess a number\n")
    return user_number

def compare_results(secret_number,user_number):
    s=int(secret_number)
    n=int(user_number)
    return s==n


