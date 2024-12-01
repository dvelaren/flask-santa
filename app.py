from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")  # GET Method
def home():
    """
    Handles the root URL of the application.

    Returns:
        str: A simple HTML string with a greeting message.
    """
    return render_template("home.html", my_name="David")


@app.route("/about")  # GET Method
def about():
    """
    Handles the root URL of the application.

    Returns:
        str: A simple HTML string with a greeting message.
    """
    return render_template(
        "about.html",
        about_text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam nec pur",
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8989)
