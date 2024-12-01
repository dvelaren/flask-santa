from flask import Flask, abort, request
from utils import find_modify_user

app = Flask(__name__)
users = [
    {
        "id": 1,
        "name": "Santa",
        "age": 25,
        "occupation": "Software Engineer",
        "hobbies": ["Reading", "Coding", "Gaming"],
    },
    {
        "id": 2,
        "name": "David",
        "age": 30,
        "occupation": "Data Scientist",
        "hobbies": ["Hiking", "Cooking", "Photography"],
    },
    {
        "id": 3,
        "name": "Esteban",
        "age": 22,
        "occupation": "Graphic Designer",
        "hobbies": ["Drawing", "Painting", "Traveling"],
    },
    {
        "id": 4,
        "name": "Jorge",
        "age": 35,
        "occupation": "Teacher",
        "hobbies": ["Reading", "Teaching", "Traveling"],
    },
    {
        "id": 5,
        "name": "Luis",
        "age": 28,
        "occupation": "Marketing Specialist",
        "hobbies": ["Social Media", "Content Creation", "Networking"],
    },
]


@app.errorhandler(404)
def not_found(error):
    return {"error": error.description}, 404


@app.route("/users")
def get_users():
    """
    Retrieve a list of users.

    Returns:
        dict: A dictionary containing a list of users.
    """
    return {"users": users}


@app.route("/users/<int:user_id>")
def get_user(user_id):
    """
    Retrieve a user by their user ID.

    Args:
        user_id (int): The ID of the user to retrieve.

    Returns:
        dict: The user dictionary if found, otherwise an empty list.
    """
    user = find_modify_user(user_id, users)
    if user is None:
        abort(404, f"User with id {user_id} not found")
    return user


@app.put("/users/<int:user_id>")
def update_user(user_id):
    global users
    user_new_props = request.get_json()
    user = find_modify_user(user_id, users, user_new_props)
    if user is None:
        abort(404, f"User with id {user_id} not found")
    return user


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8989)
