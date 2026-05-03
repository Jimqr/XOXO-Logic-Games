import sys
import subprocess
import os
import display
import json

user_input = sys.argv[1]

intro = display.intro

with open("users.json", "r") as file:
    data = json.load(file)
    for ndata in data:
        if ndata['username'] == user_input:
            score = ndata['score']

menu = f"""
    Welcome to XOXO Game!
    
    1. Math Operation
    2. What's New? 
    
    Username: {user_input}
    Score: {score}
    
    `CTRL + C` to exit"""

os.system('clear')

print(intro, menu)

def choice():
    num = int(input("Input to continue: "))
    try:
        if num == 1:
            subprocess.run(["python", "mathquiz.py", user_input])
        elif num == 2:
            os.system('clear')
            print(intro, menu)
            print("None")
            return
        else:
            num = int(input("Please try again. Choose in the menu: "))
    except KeyboardInterrupt:
        print("Keyboard Interrupted. Exited.")
        sys.exit()

while True:
    choice()