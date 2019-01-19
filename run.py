import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/") # this is the 'decorator'
def index(): # this is the 'view'
    return render_template("index.html")

@app.route("/about") # this is the 'decorator'
def about(): # this is the 'view'
    return render_template("about.html")

@app.route("/contact") # this is the 'decorator'
def contact(): # this is the 'view'
    return render_template("contact.html")

@app.route("/careers") # this is the 'decorator'
def careers(): # this is the 'view'
    return render_template("careers.html")

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            #(original) port=int(os.environ.get("PORT")),
            #(with added port 33507) port=int(os.environ.get("PORT", 33507)),
            port=(os.environ.get("PORT")), # remove int from port=int
            debug=True)