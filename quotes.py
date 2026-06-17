from flask import Flask, render_template
from datetime import date

app = Flask(__name__)

quotes = [
    "Believe in yourself and all that you are.",
    "Every day is a second chance.",
    "Push yourself, because no one else is going to do it for you.",
    "Dream big and dare to fail.",
    "Start where you are. Use what you have. Do what you can.",
    "Stay positive, work hard, make it happen.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "Your future is created by what you do today, not tomorrow.",
    "Small progress is still progress.",
    "Discipline is choosing between what you want now and what you want most.",
    "Success doesn't come from motivation. It comes from consistency.",
    "The harder you work for something, the greater you'll feel when you achieve it."
]

@app.route("/")
def home():
    today = date.today()

    # Same quote for the entire day
    index = today.toordinal() % len(quotes)
    quote = quotes[index]

    return render_template(
        "index.html",
        quote=quote,
        current_date=today.strftime("%B %d, %Y")
    )

if __name__ == "__main__":
    app.run(debug=True)