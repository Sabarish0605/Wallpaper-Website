from flask import Flask, render_template, request, redirect, jsonify
import sqlite3

app = Flask(__name__)

# Create a database table if it doesn't exist
def init_db():
    conn = sqlite3.connect("contact.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            message TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

init_db()  # Initialize the database

# Route to serve the contact page (if using Flask templating)
@app.route("/contact")
def contact_page():
    return render_template("contact.html")  # Only needed if you move contact.html to templates folder

# API route to handle form submission
@app.route("/submit_contact", methods=["POST"])
def submit_contact():
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]

    conn = sqlite3.connect("contact.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)", (name, email, message))
    conn.commit()
    conn.close()

    return jsonify({"message": "Form submitted successfully!"})

if __name__ == "__main__":
    app.run(debug=True)
