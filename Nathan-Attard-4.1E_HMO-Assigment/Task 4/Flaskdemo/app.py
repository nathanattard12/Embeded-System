from flask import Flask
import datetime

app = Flask(__name__)

@app.route("/")


def weather_station():
    # get the current date and format it
    date_now = datetime.datetime.today()
    formatted_date = date_now.strftime("%A, %d %B %Y, %H:%M")
    
    # create the HTML string for the page
    html = f"""
        <html style="backround-color: black;">
            <head>
                <title>Weather Station</title>
            </head>
            <body style="background-color: blue; text-align: center; margin-top: 40px; color: white;">
                <h1>Weather Station!</h1>
                <div style="background-color: grey; text-align:center; margin-top: 30px; color: white; padding: 5px;">
                    <h1>Email</h1>
                    
                </div>
                <div style="background-color: black; text-align:center; color: white; padding: 5px;">
                    <h1>{formatted_date}</h1>
                <div style="background-color: cyan; margin-top: 50px; color: black; padding: 30px; float: left; padding-right: 1280px; text-align:center;">
                    <h1> Temperture 25 *</h1>
                </div>
            </body>
        </html>
    """
    return html


users = {"nathan": "Nathan Attard",
         "isaac": "Isaac Attard"}

@app.route("/user")
def show_user_overview():
    users_str = "<br>".join(users.values())
    return "<body style='background-color: blue;'><h1>Our users</h1><br>{}</body>".format(users_str)

@app.route("/user/<username>")
def show_user_profile(username):
    return "<body style='background-color: blue;'><b>User</b><br> {}</body>".format(username)

if __name__ == '__main__':
    app.run(debug=True)

