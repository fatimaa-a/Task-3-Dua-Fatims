from flask import Flask, render_template, request
from data import items
from recommender import recommend

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    results = []

    if request.method == "POST":
        user_input = request.form.get("interests", "")
        user_prefs = [i.strip().lower() for i in user_input.split(",")]

        results = recommend(user_prefs, items)

    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)