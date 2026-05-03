# XOXO-Logic-Games

## 📁 File Structure
 * start.py: The entry point of the application. Handles user login and registration.
 * main.py: The main dashboard after logging in.
 * mathquiz.py: Contains the logic for the math games and score updates.
 * display.py: Stores the ASCII art header and versioning information.
 * users.json: A JSON database storing usernames and their respective scores.
## 🎮 How to Play
 1. **Launch the Game**:
   Start the application by running the start.py script:
   ```bash
   python start.py
   
   ```
  NOTE: MAKE SURE YOU INSTALLED ALL THE MODULE, OTHERWISE THE PROGRAM WILL NOT WORK.
  
 2. **Login/Register**:
   * Enter an existing username (e.g., yang, meme, or aldrin).
   * If your name isn't found, follow the prompts to register.
 3. **Navigate the Menu**:
   * Choose **1** to start a Math Operation quiz.
   * Select your preferred operator (Addition, Subtraction, etc.).
 4. **Solve Problems**:
   * Input your answers. For division, round your answer to **two decimal places**.
   * Type exit to return to the quiz selection menu.
   * Use CTRL + C at any time to exit the program.
## 📝 Example users.json Format
The game stores user data in the following format:
```json
[
    {
        "username": "example_user",
        "score": 10
    }
]

```
## 🤝 Credits
Built by **Jim**

Just got bored, so I create this very simple project.
