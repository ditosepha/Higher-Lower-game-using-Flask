from flask import Flask
import random
app = Flask(__name__)


@app.route("/")
def home_HTML():
    return "<h1>Guess a number between 0 and 9</h1><img src='https://i.giphy.com/3o7aCSPqXE5C6T8tBC.webp'>"

@app.route("/<int:num>")
def detect_number(num):
    global RANDOM_NUM
    if num == RANDOM_NUM:
        return "<h1>You found me!</h1><img src='https://i.giphy.com/4T7e4DmcrP9du.webp'>"
    elif num > RANDOM_NUM:
        return "<h1>Too high, try again!</h1><img src='https://i.giphy.com/3o6ZtaO9BZHcOjmErm.webp'>"
    elif num < RANDOM_NUM: 
        return "<h1>Too low, try again!</h1><img src='https://i.giphy.com/jD4DwBtqPXRXa.webp'>"


if __name__ == "__main__":
    RANDOM_NUM = random.randint(0,9)
    app.run(debug=True)
  
