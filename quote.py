from flask import Flask, jsonify
import random

app = Flask(__name__)

# 📚 List of inspirational quotes
quotes = [
    "Believe in yourself and all that you are.",
    "Every day is a second chance.",
    "Push yourself, because no one else is going to do it for you.",
    "Dream big and dare to fail.",
    "Start where you are. Use what you have. Do what you can.",
    "Stay positive, work hard, make it happen.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts."
]


@app.route('/')
def get_quote():
    quote = random.choice(quotes)
    return jsonify({
        "quote": quote
    })


if __name__ == '__main__':
    app.run(debug=True)
