Trivia Game
Overview

The Trivia Game is a Python application with a Tkinter GUI that fetches true/false questions from the Open Trivia DB API. Test your knowledge by answering these questions, and see how you score!
Features
    Boolean Questions: True/False questions from the Open Trivia DB API.
    Customizable Session Length: Change the number of questions per session by adjusting a parameter in the code.
    Simple GUI: Easy-to-use interface for answering questions.

Getting Started
Prerequisites
Ensure you have Python 3.x installed. You’ll also need the requests library. If you don’t have it, install it using:
-pip install requests

Configuration

To change the number of questions per session, update the amount parameter in the param dictionary within the script.

param = {
    'amount': 10,  # Number of questions per session
    'type': 'boolean'
}

Update the amount: Set the desired number of questions.

Example: For 5 questions, use:
param = {
      'amount': 5,
      'type': 'boolean'
}

Playing the Game

    Start the Game: Run the script with Python.
    Answer Questions: Click on the "Check" or "Cross" for each question.
    View Results: See your score and correct answers after the session.
