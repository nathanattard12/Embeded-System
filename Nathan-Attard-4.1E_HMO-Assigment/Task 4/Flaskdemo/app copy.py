from flask import Flask

app=Flask(__name__)

@app.route("/")
def hello():
    return "Hello world!"

users = {"nathan": "Nathan Attard",
         "isaac": "Isaac Attard"
         }


@app.route("/user")
def show_user_overview():
    users_str = "<br>".join(users.values())
    return "<h1>Our users</h1><br>{}".format(users_str)

@app.route("/user/<username>")
def show_user_profile(username):
    # show the user profile for that user
    return "<b>User</b><br> %s" % username

app.run(port=5001)
if __name__ == '__main__':
    app.run()