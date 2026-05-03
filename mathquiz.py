import random
import os
import subprocess
import sys
import json

os.system("clear")

user_input = sys.argv[1]
users = []
get_score = 1

def nscore():
    with open("math_users.json", "r") as file:
            data = json.load(file)
            for ndata in data:
                if ndata["username"] == user_input:
                    ndata["score"] += get_score
                    break
                
            with open("math_users.json", "w") as file:
                json.dump(data, file, indent = 4)

def menu():
    with open("math_users.json", "r") as file:
        data = json.load(file)
        for ndata in data:
            if ndata["username"] == user_input:
                score = ndata["score"]
    print(f"""
    Welcome to Simple Math Quiz!
    Choose a number to start the quiz!
    
    1. Addition
    2. Substraction
    3. Multiplication
    4. Division
    
    Username: {user_input}
    Score: {score}
    """)
    while True:
        try:
            global start
            start = int(input("Enter a number to start the quiz: "))
            break
        except Exception:
            print("Make sure the input value is numerical.\n")
        except KeyboardInterrupt:
            print("\nKeyboard Interrupted. Exited.")
            
    os.system("clear")

def op(a, b, start):
    if start == 1:
        ans = a + b
        ope = "+"
    elif start == 2:
        ans = a - b
        ope = "-"
    elif start == 3:
        ans = a * b
        ope = "*"
    elif start == 4:
        ans = a / b
        ope = "/"
    else:
        return None, None
            
    return ans, ope

def check():
    while True:
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        
        ans, ope = op(a, b, start)
        
        while True:
            try:
                user_ans = input(f"{a} {ope} {b} ? ")
                if user_ans == "exit":
                    os.system('clear')
                    return
                else:
                    user_ans = float(user_ans)
                    break
            except Exception:
                print("Make sure the input value is numerical.\n")
            except KeyboardInterrupt:
                print("\nKeyboard Interrupted. Exited.")
        if start == 4:
            if round(user_ans, 2) == round(ans, 2):
                print("correct")
                nscore()
            else:
                print(f"incorrect. the correct answer is {round(ans, 2)}")
        else:
            if user_ans == ans:
                print("correct")
                nscore()
            else:
                print(f"incorrect. the correct answer is {ans}")

while True:
    menu()
    print("Answer the following question below. Round off up to two decimal places only. Prompt `exit` to return back to menu.\n")
    check()