from flask import Flask, request, jsonify
import re

app = Flask(__name__)

students = {}
next_id = 1


def validate_student(data):
    if not data:
        return "Request body is required"

    name = data.get("name")
    age = data.get("age")
    email = data.get("email")

    if not isinstance(name, str) or not name.strip():
        return "Name must be a non-empty string"

    if len(name.strip()) < 2 or len(name.strip()) > 50:
        return "Name must contain 2 to 50 characters"

    if not isinstance(age, int) or isinstance(age, bool):
        return "Age must be an integer"

    if age < 16 or age > 100:
        return "Age must be between 16 and 100"

    if not isinstance(email, str) or not re.match(
        r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email
    ):
        return "Invalid email address"

    return None


@app.route("/")
def home():
    return jsonify({
        "message": "Student Management API is running",
        "version": "1.0"
    })


@app.route("/students", methods=["POST"])
def add_student():
    global next_id

    data = request.get_json(silent=True)
    error = validate_student(data)

    if error:
        return jsonify({"error": error}), 400

    student = {
        "id": next_id,
        "name": data["name"].strip(),
        "age": data["age"],
        "email": data["email"]
    }

    students[next_id] = student
    next_id += 1

    return jsonify({
        "message": "Student added successfully",
        "student": student
    }), 201


@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(list(students.values())), 200


@app.route("/students/<int:student_id>", methods=["GET"])
def get_student(student_id):
    student = students.get(student_id)

    if not student:
        return jsonify({"error": "Student not found"}), 404

    return jsonify(student), 200


@app.route("/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    if student_id not in students:
        return jsonify({"error": "Student not found"}), 404

    data = request.get_json(silent=True)
    error = validate_student(data)

    if error:
        return jsonify({"error": error}), 400

    students[student_id].update({
        "name": data["name"].strip(),
        "age": data["age"],
        "email": data["email"]
    })

    return jsonify({
        "message": "Student updated successfully",
        "student": students[student_id]
    }), 200


@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    if student_id not in students:
        return jsonify({"error": "Student not found"}), 404

    del students[student_id]

    return jsonify({
        "message": "Student deleted successfully"
    }), 200


if __name__ == "__main__":
    app.run(debug=True)