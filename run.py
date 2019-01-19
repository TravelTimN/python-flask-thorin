import os
import json
from flask import Flask, render_template

app = Flask(__name__)

tabTitle = " | "

@app.route("/") # this is the 'decorator'
def index(): # this is the 'view'
    pageTitle = "Thorin & Company"
    return render_template("index.html", page_title=pageTitle)

@app.route("/about") # this is the 'decorator'
def about(): # this is the 'view'
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    pageTitle = "About"
    return render_template("about.html", page_title=pageTitle, tab_title=pageTitle + tabTitle, company=data)

@app.route("/contact") # this is the 'decorator'
def contact(): # this is the 'view'
    pageTitle = "Contact"
    return render_template("contact.html", page_title=pageTitle, tab_title=pageTitle + tabTitle)

@app.route("/careers") # this is the 'decorator'
def careers(): # this is the 'view'
    pageTitle = "Careers"
    return render_template("careers.html", page_title=pageTitle, tab_title=pageTitle + tabTitle)

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            #(original) port=int(os.environ.get("PORT")),
            #(with added port 33507) port=int(os.environ.get("PORT", 33507)),
            port=(os.environ.get("PORT")), # remove int from port=int
            debug=True)