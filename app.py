from flask import Flask, jsonify, render_template, request, redirect, url_for
from pymongo import MongoClient
import json

app = Flask(__name__)

# MongoDB Atlas connection
# Replace with your connection string from MongoDB Atlas
client = MongoClient("mongodb+srv://sonupd8294_db_user:o8O2G8gjAOc5JYQ1@cluster0.setbgfa.mongodb.net/")
db = client["flask_assignment"]
collection = db["submissions"]

# 1. API route: return JSON data from file
@app.route("/api")
def api():
    with open("data.json", "r") as f:
        data = json.load(f)
    return jsonify(data)

# 2. Frontend form
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            name = request.form.get("name")
            email = request.form.get("email")

            # Insert into MongoDB Atlas
            collection.insert_one({"name": name, "email": email})

            # Redirect on success
            return redirect(url_for("success"))

        except Exception as e:
            # Show error without redirect
            return render_template("form.html", error=str(e))

    return render_template("form.html")

@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)
