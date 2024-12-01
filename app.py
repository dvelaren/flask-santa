from flask import Flask

app = Flask(__name__)


@app.route("/")  # GET Method
def hello_world():
    """
    Handles the root URL of the application.

    Returns:
        str: A simple HTML string with a greeting message.
    """
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8989)
