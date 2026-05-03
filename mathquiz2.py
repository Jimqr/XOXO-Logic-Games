import sys
import subprocess
import json

try:
    with open("math_users.json", "r") as file:
        data = json.load(file)
except FileNotFoundError:
    with open("math_users.json", "x") as file:
        tada = json.load(file)
  
users = [item["username"] for item in data] 

try:
    user_input = input("Enter your username to login: ")
    if user_input in users:
        subprocess.run(["python", "mathquiz.py", user_input])
    else:
        no_user = input("No user found. Would you like to register as new user? [yes / no] ")
        if no_user == "yes":
            new_user  = input("Enter your new username to register: ")
            if new_user in users:
                print(f"{new_user} exists already. Please choose another username.")
            else:
                data.append({
                        "username": new_user,
                        "score": 0
                        })
                with open("math_users.json", "w") as file:
                    json.dump(data, file, indent=4)
                    print(f"Welcome {new_user}! You can login now! Please run the program again.")
        else:
            print("run `python mathquiz2.py` to continue again.")
            sys.exit()
except KeyboardInterrupt:
    print("Keyboard Interrupted. Exited.")
                    