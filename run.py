import os
import json
from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "beartravels"

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

@app.route("/about/<member_name>") # this is the 'decorator'
def about_member(member_name): # this is the 'view'
    member = {}

    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["link"] == member_name:
                member = obj
    
    return render_template("member.html", member=member)

@app.route("/careers") # this is the 'decorator'
def careers(): # this is the 'view'
    pageTitle = "Careers"
    return render_template("careers.html", page_title=pageTitle, tab_title=pageTitle + tabTitle)

@app.route("/contact", methods=["GET", "POST"]) # this is the 'decorator'
def contact(): # this is the 'view'
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(request.form["name"]))
        #print(request.form)
        #print(request.form["email"])

    pageTitle = "Contact"
    return render_template("contact.html", page_title=pageTitle, tab_title=pageTitle + tabTitle)

if __name__ == "__main__":
    """
    app.run(host=os.environ.get("IP"),
            #port=int(os.environ.get("PORT")), # with port=int (the original)
            #port=int(os.environ.get("PORT", 33507)), # with added port 33507
            #port=int(os.environ.get("PORT", 5000)), # with added port 5000
            port=(os.environ.get("PORT")), # works during deployment
            debug=True)
    """
    
    app.run(host=os.getenv("IP"),
            port=os.getenv("PORT"),
            debug=False)