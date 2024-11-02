from guizero import *
import datetime

date_now = datetime.datetime.today()
formatted_date = date_now.strftime("%A, %d %B %Y, %H:%M")

app = App(title="Weather Station", bg="blue")

text = Text(app, text="Weather for today", font="Helvetica", size=30, color="white", width=80, height=2, bg="darkcyan")
email_text = Text(app, text="Email", size=25, color="white", width=80, height=1, bg="gray")

date = Text(app, text=formatted_date, bg="black", width=80, height=1, color="white", size=25)

Temp = Text(app, text="Temperature\n\n25C", width=50, height=10, bg="cyan", align="left")



Hum = Text(app, text="Humidity\n\n55C", width=50, height=10, bg="cyan", align="left")



date.tk.pack(padx=0,pady=10)
Temp.tk.pack(padx=10, pady=10)

app.display()
