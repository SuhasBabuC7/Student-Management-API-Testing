# Student Management REST API Testing

## 1. Project Overview

This project demonstrates automated REST API testing using Postman CLI and Python Flask.

The Student Management API allows users to perform CRUD (Create, Read, Update, Delete) operations on student records.

The project demonstrates functional testing, negative testing, input validation and Boundary Value Analysis.

## 2. Technology Stack

- Python
- Flask
- Postman CLI
- JavaScript Assertions
- REST API
- Git and GitHub

## 3. Project Structure

```text
Student_API_Testing/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── tests/
│   └── Student_API_Tests.postman_collection.json
│
├── reports/
│   ├── collection-run-summary.yaml
│   └── collection-run-executions.yaml
│
└── screenshots/
```

## 4. API Features

| HTTP Method | Endpoint | Description |
|---|---|---|
| GET | / | API health check |
| POST | /students | Add a student |
| GET | /students | Retrieve all students |
| GET | /students/{id} | Retrieve student by ID |
| PUT | /students/{id} | Update student |
| DELETE | /students/{id} | Delete student |

## 5. Validation Rules

- Student name must contain 2–50 characters.
- Student age must be between 16 and 100.
- Email must follow a valid email format.
- Invalid inputs are rejected with HTTP 400.
- Nonexistent student records return HTTP 404.

## 6. Installation and Execution

### Prerequisites

- Python 3.x
- Node.js and npm
- Postman CLI
- Git

### Step 1: Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Navigate to the project

```bash
cd Student_API_Testing
```

### Step 3: Create a virtual environment

```bash
python -m venv venv
```

### Step 4: Activate the environment

Windows PowerShell:

```powershell
venv\Scripts\activate
```

### Step 5: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 6: Start the Flask API

```bash
python app.py
```

The API will run at:

http://127.0.0.1:5000

### Step 7: Install Postman CLI

```bash
npm install -g postman-cli
```

### Step 8: Authenticate with Postman

```bash
postman login
```

### Step 9: Execute automated tests

Open another terminal and execute:

```bash
postman collection run ./tests/Student_API_Tests.postman_collection.json
```

### Step 10: Generate execution reports

```bash
postman collection run ./tests/Student_API_Tests.postman_collection.json --output ./reports
```

Generated YAML reports will be available in the reports directory.

## 7. Test Cases

The project includes 15 automated API test requests covering:

1. API health check.
2. Add valid student.
3. Retrieve all students.
4. Retrieve student by ID.
5. Update student details.
6. Delete student.
7. Invalid student ID.
8. Empty student name.
9. Invalid email.
10. Age below minimum.
11. Age above maximum.
12. Minimum valid age.
13. Maximum valid age.
14. Invalid age data type.
15. One-character student name.

## 8. Execution Results

Recorded successful execution:

| Metric | Result |
|---|---:|
| Total requests | 15 |
| Test scripts | 15 |
| Assertions | 20 |
| Passed assertions | 20 |
| Failed assertions | 0 |
| Assertion pass rate | 100% |
| Average response time | 14 ms |
| Execution duration | 1593 ms |

Note: These results represent the recorded execution run.

## 9. Testing Techniques

### Functional Testing
Verifies that all CRUD operations work as expected.

### Negative Testing
Checks how the API handles invalid inputs and nonexistent records.

### Boundary Value Analysis
Tests minimum and maximum allowed age values and invalid values immediately outside the permitted range.

### Assertion Testing
Uses JavaScript assertions to validate HTTP status codes and response data.

## 10. Important Note

This project uses in-memory storage. Student records are not persisted after the Flask application restarts.

The project is developed for academic demonstration and software testing purposes.

## 11. Conclusion

This project demonstrates how Postman CLI can automate REST API testing, validate application behaviour, identify input validation issues and generate execution reports.

It provides practical exposure to API testing and software quality assurance.