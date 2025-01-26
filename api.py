from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)  # Enable CORS for all origins

# Load the marks data from the JSON file
with open("marks.json", "r") as file:
    data = json.load(file)

@app.route("/")
def home():
    return "Welcome to the API! Use the /api endpoint to fetch marks."

@app.route("/api", methods=["GET"])
def get_marks():
    # Get the 'name' parameters from the query string
    names = request.args.getlist("name")
    
    # Extract marks for the given names
    marks = [next((student["marks"] for student in data if student["name"] == name), None) for name in names]
    
    return jsonify({"marks": marks})

if __name__ == "__main__":
    app.run(debug=True)
