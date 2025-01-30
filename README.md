# pAPI Application

## Description
This is a simple Flask API application that provides information including a registered email address, the current datetime in ISO 8601 format, and the GitHub URL of the project's codebase.

## Installation
To install the necessary dependencies, run the following command:

```bash
pip install -r requirements.txt
```

## Usage
To run the application, use the following command:

```bash
flask run
```

Make sure to set the `FLASK_APP` environment variable to `app.py` before running the command.

## Endpoints
- `GET /`: Returns a JSON response containing:
  - `email`: The registered email address.
  - `current_datetime`: The current datetime in ISO 8601 format.
  - `github_url`: The GitHub URL of the project's codebase.


Backlinks to:
https://hng.tech/hire/python-developers