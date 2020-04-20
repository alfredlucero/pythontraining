# export FLASK_APP=app.py
# python -m flask run
from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

# Default GET request for routes
@app.route("/templates")
def read_templates():
    return "Read Templates"

# request.form["bodykey"]
# request.args.get("key", "") -> query string
# request.cookies.get("cookie")
@app.route("/templates", methods=["POST"])
def create_template():
    print("Create Template")
    from_address = request.form["from_address"]
    subject_line = request.form["subject_line"]
    email_body = request.form["email_body"]
    # Can return JSON in a dict or use jsonify() function
    return {
        "id": 1,
        "from_address": from_address,
        "subject_line": subject_line,
        "email_body": email_body,
    }


@app.route("/templates/<int:template_id>")
def read_template_details(template_id):
    print("Read Template %d" % template_id)


@app.route("/templates/<int:template_id>", methods=["PATCH"])
def update_template(template_id):
    print("Update Template %d" % template_id)


@app.route("/templates/<int:template_id>", methods=["DELETE"])
def delete_template(template_id):
    print("Delete Template %d" % template_id)
